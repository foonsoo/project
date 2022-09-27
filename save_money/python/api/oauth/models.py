from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER(display_width=11, unsigned=True), primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255))

class SecretKey(Base):
    __tablename__ = "secretkeys"
    id = Column(INTEGER(display_width=11, unsigned=True), primary_key=True, index=True)
    skey = Column(String(255),unique=True, index=True)
    
class RegisterKey(Base):
    __tablename__ = "registerkeys"
    id = Column(INTEGER(display_width=11, unsigned=True), primary_key=True, index=True)
    regkey = Column(String(255),unique=True, index=True)