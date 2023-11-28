from flask import Flask
from models import db
from controllers.user_controller import user_blueprint
from controllers.mobile_controller import mobile_blueprint
from controllers.question_controller import question_blueprint
from controllers.review_controller import reviews_blueprint
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Set the database URI here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(user_blueprint)
app.register_blueprint(mobile_blueprint)
app.register_blueprint(question_blueprint)
app.register_blueprint(reviews_blueprint)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
