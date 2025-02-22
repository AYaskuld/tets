from flask import Flask
from src.models.user import db
from .config.server import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    from src.routes.user_routes import api
    app.register_blueprint(api)

    return app