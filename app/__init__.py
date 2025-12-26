from flask import Flask
from .config.settings import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.routes.main import main_bp
    from app.routes.logs_routes import logs_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(logs_bp)

    return app
