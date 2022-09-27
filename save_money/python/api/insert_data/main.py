from typing import List
from fastapi import Depends, FastAPI, HTTPException,status, Form, Request, status
from sqlalchemy.orm import Session
import models
import crud
import schemas
from datetime import datetime, timedelta, date
from database import SessionLocal, engine
from fastapi.responses import HTMLResponse, ORJSONResponse, JSONResponse
import json
import time
from fastapi.middleware.cors import CORSMiddleware
import logging
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

@app.get("/api/v1/money/list", response_model=List[schemas.CardUsage])
def show_money_list(db: Session = Depends(get_db), skip: int = 0, limit: int = 20):
    return db.query(models.CardUsage).order_by(models.CardUsage.used_date.desc()).offset(skip).limit(limit).all()

@app.post("/api/v1/money/insert/",response_model=List[schemas.CardUsage])
def insert_money(data: schemas.CardUsageBase, db: Session=Depends(get_db)):
    money_data = models.CardUsage(card_id=data.card_id, used_date=data.used_date, franchisee=data.franchisee, amount_used=data.amount_used)
    db.add(money_data)
    db.commit()
    return crud.check_last_insert(db)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logging.error(f"{request}: {exc_str}")
	content = {'status_code': 10422, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)