from typing import List
from fastapi import Depends, FastAPI, HTTPException,status, Form
from sqlalchemy.orm import Session
import crud
import models
import schemas
from datetime import datetime, timedelta
from redis_models import Token
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import redis
import json
import time
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.post("/api/v1/auth/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    data = {
            "access_token": access_token, 
            "token_type": "bearer"
            }
    data_dict = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return {"access_token": access_token, "token_type": "bearer", "user": user.username} ## Web Page Redirect 분리를 위함

@app.post("/api/v1/auth/signup", response_model=schemas.User)
def create_user(regkey: str, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if regkey != "ggu":
        raise HTTPException(status_code=400, detail="Registry Code Is Not Matched") 
    elif db_user:
        raise HTTPException(status_code=400, detail="User is Already In")   
    return crud.create_user(db, user=user)


@app.get("/api/v1/auth/user", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/api/v1/auth/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


