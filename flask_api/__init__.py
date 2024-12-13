from flask import Flask

def create_app():
    app = Flask(__name__)

    from flask_api.routes import api_bp as bp
    app.register_blueprint(bp, url_prefix='/dice')

    return app