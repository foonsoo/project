from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, date
from fastapi import Form


class CardUsageBase(BaseModel):
    card_id: int
    used_date: date
    franchisee: str
    amount_used: int
    card_used_type_code: Optional[int]
    
    class Config:
        orm_mode = True

class CardUsage(CardUsageBase):
    id: int

    class Config:
        orm_mode = True