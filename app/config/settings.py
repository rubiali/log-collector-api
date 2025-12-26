import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-super-secret-123")

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017"

class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")