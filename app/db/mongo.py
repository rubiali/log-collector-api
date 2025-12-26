from pymongo import MongoClient, ASCENDING
from flask import current_app

_client = None


def get_client():
    """
    Obtém o cliente de conexão com o MongoDB.
    """
    global _client
    if _client is None:
        mongo_uri = current_app.config.get("MONGO_URI")
        _client = MongoClient(mongo_uri)
    return _client


def get_db():
    """
    Obtém o banco de dados do MongoDB.
    """
    client = get_client()
    return client["log_collector"]


def setup_indexes():
    """
    Cria índices necessários para performance das consultas.
    """
    db = get_db()
    collection = db.logs

    collection.create_index([("level", ASCENDING)])
    collection.create_index([("service", ASCENDING)])
    collection.create_index([("created_at", ASCENDING)])
