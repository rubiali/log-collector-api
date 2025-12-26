from app import create_app
from app.routes.main import main_bp
from app.config.settings import DevelopmentConfig

app = create_app()

if __name__ == "__main__":
    app.register_blueprint(main_bp)
    app.config.from_object(DevelopmentConfig)
    app.run(debug=True)