from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, TIMESTAMP, text, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class UserAccount(db.Model):
    __tablename__ = 'UserAccount'
    user_ID = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255))
    user_email = Column(String(255), unique=True)
    password = Column(String(255))
    year_of_birth = Column(Integer)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    # Define a relationship with Review model
    reviews = relationship('Review', back_populates='user', cascade='all, delete-orphan')

class Mobile(db.Model):
    __tablename__ = 'mobile'
    mobile_ID = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(255))
    mobile_name = Column(String(255), unique=True)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    # Define a relationship with Review model
    reviews = relationship('Review', back_populates='mobile', cascade='all, delete-orphan')

class Review(db.Model):
    __tablename__ = "review"
    review_ID = Column(Integer, primary_key=True, autoincrement=True)
    user_ID = Column(Integer, ForeignKey('UserAccount.user_ID', ondelete='CASCADE'), nullable=False)
    mobile_ID = Column(Integer, ForeignKey('mobile.mobile_ID', ondelete='CASCADE'), nullable=False)
    question_ID = Column(Integer, ForeignKey('question.question_ID'), nullable=False)
    rating = Column(Integer)
    __table_args__ = (UniqueConstraint('user_ID', 'mobile_ID', 'question_ID', name='uq_user_mobile_question'),)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    # Define relationships with UserAccount and Mobile models
    user = relationship('UserAccount', back_populates='reviews')
    mobile = relationship('Mobile', back_populates='reviews')

class Question(db.Model):
    __tablename__ = "question"
    question_ID = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String(255), unique=True)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    # Define a relationship with Review model
    reviews = relationship('Review', back_populates='question', cascade='all, delete-orphan')

class UserOverAllReview(db.Model):
    __tablename__ = 'useroverallreview'
    id = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('UserAccount.user_ID', ondelete='CASCADE'), nullable=False)
    mobile_ID = Column(Integer, ForeignKey('mobile.mobile_ID', ondelete='CASCADE'), nullable=False)
    review = Column(String(255))
