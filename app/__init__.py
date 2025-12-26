from flask import Flask
from .config.settings import DevelopmentConfig
from app.db.mongo import setup_indexes

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.routes.logs_routes import logs_bp
    from app.routes.health_routes import health_bp

    app.register_blueprint(logs_bp)
    app.register_blueprint(health_bp)

    with app.app_context():
        setup_indexes()

    return app
