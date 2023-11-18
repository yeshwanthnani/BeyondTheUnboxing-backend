
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, text, Integer

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer)
    user_name = Column(String(255), primary_key=True)
    user_email = Column(String(255))
    password = Column(String(255))
    year_of_birth = Column(Integer)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

class Mobile(Base):
    __tablename__ = 'mobile'
    mobile_id = Column(Integer)
    brand = Column(String(255))
    mobile_name = Column(String(255), primary_key=True)

