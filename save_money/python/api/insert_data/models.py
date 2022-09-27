from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, Date
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class CardUsage(Base):
    __tablename__ = "card_usage"

    id = Column(INTEGER, primary_key=True, index=True)
    card_id = Column(INTEGER)
    used_date = Column(Date)
    franchisee = Column(String(30))
    amount_used = Column(INTEGER)
    card_used_type_code = Column(INTEGER)