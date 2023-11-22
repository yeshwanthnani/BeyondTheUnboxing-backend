from datetime import datetime
from sqlalchemy.orm import Session
from model import UserAccount

class TestDataInserter:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_name, user_email, password, year_of_birth):
        UserAcc = UserAccount(
            user_name=user_name,
            user_email=user_email,
            password=password,
            year_of_birth=year_of_birth,
        )
        self.session.add(UserAcc)
        self.session.commit()

    def insert_sample_data(self):
        # Sample data for the User table
        sample_users = [
            {
                'user_name': 'user1',
                'user_email': 'user1@example.com',
                'password': 'password1',
                'year_of_birth': 1990,
            },
            {
                'user_name': 'user2',
                'user_email': 'user2@example.com',
                'password': 'password2',
                'year_of_birth': 1985,
            },
            # Add more sample user data as needed
        ]

        # Insert sample data into the User table
        for user_data in sample_users:
            self.create_user(**user_data)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Replace 'your_database_url' with the actual URL of your database
    engine = create_engine('postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create an instance of TestDataInserter and call the insert_sample_data method
    data_inserter = TestDataInserter(session)
    data_inserter.insert_sample_data()

    # Close the session
    session.close()
