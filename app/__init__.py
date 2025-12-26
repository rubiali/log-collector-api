from flask import Flask
from .config.settings import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    
    return app
