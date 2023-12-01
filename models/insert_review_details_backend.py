from sqlalchemy.orm import Session
from model import UserAccount, Mobile, Question, Review

class TestDataInserter:
    def __init__(self, session: Session):
        self.session = session


    def create_review_data(self,user_ID,mobile_ID,question_ID,rating):
        rev = Review(
            user_ID = user_ID,
            mobile_ID = mobile_ID,
            question_ID = question_ID,
            rating = rating,
        )

        self.session.add(rev)
        self.session.commit()

    def insert_review_data(self,user_ID, mobile_ID):
        for i in range(1,11):
            rating_data = {
                'user_ID': user_ID,
                'mobile_ID': mobile_ID,
                'question_ID': i,
                'rating': i,
            }
            self.create_review_data(**rating_data)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Replace 'your_database_url' with the actual URL of your database
    engine = create_engine('postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create an instance of TestDataInserter and call the insert_sample_data method
    data_inserter = TestDataInserter(session)
    data_inserter.insert_review_data(user_ID=91, mobile_ID=54)  # Specify the user_id for which you want to insert reviews

    # Close the session
    session.close()