from flask import Flask
from .config.settings import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    app.config.from_object(config_class)
    
    return app
