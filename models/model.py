from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, TIMESTAMP, text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Float
from sqlalchemy.orm import declarative_base

db = SQLAlchemy()

Base = declarative_base()
metadata = Base.metadata

class UserAccount(db.Model):
    __tablename__ = 'UserAccount'
    user_ID = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255))
    user_email = Column(String(255))
    password = Column(String(255))
    year_of_birth = Column(Integer)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    # Define a relationship with Review model
    reviews = relationship('Review', backref='user', lazy=True)
    # Define a relationship with UserIndividualReview model
    # user_individual_reviews = relationship('UserIndividualReview', back_populates='user_account', lazy=True)

class Mobile(db.Model):
    __tablename__ = 'mobile'
    mobile_ID = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(255))
    mobile_name = Column(String(255))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    # Define a relationship with Review model
    reviews = relationship('Review', back_populates='mobile', lazy=True)

class Review(db.Model):
    __tablename__ = "review"
    review_ID = Column(Integer, primary_key=True, autoincrement=True)
    user_ID = Column(Integer, ForeignKey('UserAccount.user_ID'), nullable=False)
    mobile_ID = Column(Integer, ForeignKey('mobile.mobile_ID'), nullable=False)
    question_ID = Column(Integer, ForeignKey('question.question_ID'), nullable=False)
    rating = Column(Integer)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    # Define a relationship with UserIndividualReview model
    # user_individual_reviews = relationship('UserIndividualReview', back_populates='review',
    #                                       primaryjoin="and_(Review.user_ID == foreign(UserIndividualReview.user_ID), Review.mobile_ID == foreign(UserIndividualReview.mobile_ID))")
    # Define a relationship with Mobile model
    mobile = relationship('Mobile', back_populates='reviews')

class Question(db.Model):
    __tablename__ = "question"
    question_ID = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String(255), unique=True)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    # Define a relationship with Review model
    reviews = relationship('Review', backref='question', lazy=True)

# class UserIndividualReview(db.Model):
#     __tablename__ = 'user_individual_reviews'
#     id = Column(Integer, primary_key=True)
#     user_ID = Column(Integer, ForeignKey('UserAccount.user_ID'), nullable=False)
#     mobile_ID = Column(Integer, ForeignKey('mobile.mobile_ID'), nullable=False)
#     question_ID = Column(Integer, nullable=False)
#     rating = Column(Float, nullable=False)
#
#     # Define relationships with UserAccount, Mobile, and Review models
#     user_account = relationship('UserAccount', back_populates='user_individual_reviews')
#     mobile = relationship('Mobile', back_populates='reviews')
#     review = relationship('Review', back_populates='user_individual_reviews')
