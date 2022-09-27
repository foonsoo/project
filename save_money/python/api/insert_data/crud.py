from sqlalchemy.orm import Session
import models

def check_last_insert(db: Session,skip: int = 0, limit: int = 1):
    return db.query(models.CardUsage).order_by(models.CardUsage.id.desc()).offset(skip).limit(limit).all()