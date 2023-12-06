from flask import Blueprint, jsonify, make_response
from models.model import Question, db
from flask import request
from models.Constants import HttpStatus, ResponseMessages
from DBLayer.Questionhandler import QuestionHandler
from models.exceptions import QuestionAlreadyExists, QuestionDoesNotExists

question_blueprint = Blueprint('question', __name__, url_prefix='/api/v1/')


"""-----------------endpoints---------------------:

 create :        POST     /api/v1/question/<int:question_id>/  (to create question)
 get_question:   GET      /api/v1/question/<int:question_id>/   (to get question)"""


@question_blueprint.route('question/', methods=['POST'])
def create_question():
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return make_response(jsonify({'error': 'Unsupported Media Type'}), HttpStatus.UN_SUPPORTED_MEDIA_TYPE.value)
        data = request.get_json()
        required_field = 'question_text'
        if required_field not in data:
            return make_response((jsonify({'error': f'Missing required field: {required_field}'})),
                                 HttpStatus.BAD_REQUEST.value)
        # create new question

        new = QuestionHandler.create_question(
            data['question_text']
        )
        response_data = {
            'message': ResponseMessages.CREATED.value,
            'question_ID': new.question_ID
        }

        return make_response(jsonify(response_data), HttpStatus.CREATED.value)

    except QuestionAlreadyExists as e:

        # Handle other potential exceptions
        return make_response(jsonify({'error': e.message}), HttpStatus.BAD_REQUEST.value)


@question_blueprint.route('question/<int:question_id>', methods=['GET'])
def get_questions(question_id):
    try:
        ques = QuestionHandler.get_question(question_id)
        return make_response(jsonify(ques), HttpStatus.SUCCESS.value)
    except QuestionDoesNotExists as e:
        return make_response(jsonify({'message': e.message}), HttpStatus.BAD_REQUEST.value)
