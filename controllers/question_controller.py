from flask import Blueprint, jsonify
from models.model import Question, db
from flask import request


question_blueprint = Blueprint('question', __name__, url_prefix='/api/v1/')

# endpoints:
#  GET /api/v1/question/<int:question_id>  (to get question)
#  POST /api/v1/question/register          (to register new question)
@question_blueprint.route('question/<int:question_id>', methods=['GET'])
def get_questions(question_id):
    ques = Question.query.get(question_id)

    if ques:
        question_data = {
            'question_ID': ques.question_ID,
            'question_text': ques.question_text,
            'created_on': ques.created_on,
        }

        return jsonify(question_data)
    else:
        return jsonify({'message': 'Question does not exist'}), 404


@question_blueprint.route('question/all', methods=['GET'])
def get_all_questions():
    ques_all = Question.query.all()

    questions_data = []

    for every_question in ques_all:

        all_questions_data = {

            'question_ID': every_question.question_ID,
            'question_text': every_question.question_text,
            'created_on': every_question.created_on,
        }

        questions_data.append(all_questions_data)


    if questions_data:
        return jsonify(questions_data)
    else:
        return jsonify({'message': 'No Questions found'}), 404

@question_blueprint.route('/register',methods=['POST'])
def register():
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type'}), 415

        data = request.get_json()

        required_fields = ['question_text']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # create new question
        new = Question(
            question_text = data['question_text']
        )

        db.session.add(new)
        db.session.commit()

        response_data = {
            'message': 'New question entry created successfully',
            'question_ID': new.question_ID
        }

        return jsonify(response_data), 201

    except Exception as e:

        # Handle other potential exceptions
        return jsonify({'error': str(e)}), 500