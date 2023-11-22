from sqlalchemy.orm import Session

from model import Question


class TestDataInserter:
    def __init__(self, session: Session):
        self.session = session


    def create_Questions(self, question_text):
        ques= Question(
            question_text=question_text,
        )
        self.session.add(ques)
        self.session.commit()

    def insert_questions(self):
        questions=[
            {
                'question_text': "1.Performance: How would you rate the mobile device's overall performance in your day-to-day use? Consider aspects like speed, responsiveness, and how well it handles multiple tasks.(1 to 5)"
            },
            {
                'question_text': "2.Battery Life: Evaluate the mobile device's battery life based on its ability to last throughout your typical day including fast charge, battery discharge. How satisfied are you? (1 to 5)"
            },
            {
                'question_text': "Camera:Rate the quality of the cameras for capturing photos and videos on a scale from 1 to 5, where 1 is the least satisfied and 5 is the most satisfied."
            },
            {
                'question_text': "Display: How would you rate the display quality, including outdoor brightness, colour accuracy, and resolution? "
            },
            {
                'question_text': "Durability:On a scale of 1 to 5, how would you rate the build quality of your mobile device?"
            },
            {
                'question_text': "Software and User Interface: How satisfied are you with the mobile's software user interface? Use a scale of 1 to 5."
            },
            {
                'question_text': "Communication performances:Rate the device's performance in communication features, including call quality and connectivity via Wi-Fi and Bluetooth. Use a scale from 1 to 5."
            },
            {
                'question_text': "Software and Updates:Rate your satisfaction with the mobile device's operating system and the frequency of software updates"
            },
            {
                'question_text': "Value for Money:Considering the features and performance, do you feel the mobile device offers good value for money? "
            },
            {
                'question_text': "Would you recommend anyone to purchase your mobile right today ? Yes/No"
            }
        ]


        for every_question in questions:
            self.create_Questions(**every_question)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Replace 'your_database_url' with the actual URL of your database
    engine = create_engine('postgresql+psycopg2://postgres:Nani8901@database-staging.cq5odtnxninx.us-east-1.rds.amazonaws.com/MyDataBase')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create an instance of TestDataInserter and call the insert_sample_data method
    data_inserter = TestDataInserter(session)
    data_inserter.insert_questions()

    # Close the session
    session.close()