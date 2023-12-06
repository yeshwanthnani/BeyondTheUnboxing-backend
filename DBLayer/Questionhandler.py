from models.model import Question, db
from sqlalchemy.exc import IntegrityError
from models.exceptions import Failed,QuestionAlreadyExists,QuestionDoesNotExists


class QuestionHandler():

    def __init__(self):
        return

    @staticmethod
    def create_question(question_text):
        try:
            new_question = Question(
                question_text=question_text
            )
            db.session.add(new_question)
            db.session.commit()
            return new_question
        except Exception as e:
            raise QuestionAlreadyExists()




    @staticmethod
    def get_question(question_ID):
        ques = Question.query.get(question_ID)
        if ques:
            response = {
                "question_ID":ques.question_ID,
                "question_text":ques.question_text
            }
            return response
        elif ques is None:
            raise QuestionDoesNotExists

