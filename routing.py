from controllers.user_controller import user_blueprint
from controllers.mobile_controller import mobile_blueprint
from controllers.question_controller import question_blueprint
from controllers.review_controller import reviews_blueprint

def register_routes(app):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(mobile_blueprint)
    app.register_blueprint(question_blueprint)
    app.register_blueprint(reviews_blueprint)
    # Add more register_blueprint calls for other controllers
