from sqlalchemy.orm import Session
from model import Mobile

class TestDataInserter:
    def __init__(self, session: Session):
        self.session = session


    def create_mobile_data(self, brand, mobile_name):
        mob = Mobile(

            brand=brand,
            mobile_name=mobile_name,
        )
        self.session.add(mob)
        self.session.commit()

    def insert_mobile_data(self):
        mobile_attributes = [
            {
                'brand': 'samsung',
                'mobile_name': 'S23 Ultra',
            },
            {
                'brand': 'Oneplus',
                'mobile_name': '11',
            },
            {
                'brand': 'Apple',
                'mobile_name': 'Iphone 15',
            }
        ]
        # Insert mobile data into the User table
        for user_data in mobile_attributes:
            self.create_mobile_data(**user_data)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Replace 'your_database_url' with the actual URL of your database
    engine = create_engine('postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create an instance of TestDataInserter and call the insert_sample_data method
    data_inserter = TestDataInserter(session)
    data_inserter.insert_mobile_data()

    # Close the session
    session.close()
