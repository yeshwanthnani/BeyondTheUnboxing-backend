
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, text, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

class UserAccount(Base):
    __tablename__ = 'UserAccount'
    user_ID = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255))
    user_email = Column(String(255))
    password = Column(String(255))
    year_of_birth = Column(Integer)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    reviews = relationship('Review', backref='user', lazy=True)

class Mobile(Base):
    __tablename__ = 'mobile'
    mobile_ID = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(255))
    mobile_name = Column(String(255))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    reviews = relationship('Review', backref='mobile', lazy=True)
class Review(Base):
    __tablename__ = "review"
    review_ID = Column(Integer, primary_key=True, autoincrement=True)
    user_ID = Column(Integer, ForeignKey('UserAccount.user_ID'), nullable=False)
    mobile_ID = Column(Integer, ForeignKey('mobile.mobile_ID'), nullable=False)
    question_ID = Column(Integer, ForeignKey('question.question_ID'), nullable=False)
    rating = Column(Integer)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))



class Question(Base):
    __tablename__ = "question"
    question_ID = Column(Integer, primary_key=True)
    question_text = Column(String(255), unique=True)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    reviews = relationship('Review', backref='question', lazy=True)


# class specifications(Base):
#     __tablename__ = "mobile specifications"
#     mob_spec_ID = Column(Integer, primary_key=True)
#     specs = Column(String(255))
#     created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

