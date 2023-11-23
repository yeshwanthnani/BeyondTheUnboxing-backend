from controllers.user_controller import user_blueprint

def register_routes(app):
    app.register_blueprint(user_blueprint)
    # Add more register_blueprint calls for other controllers
