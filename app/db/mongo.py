from pymongo import MongoClient
from flask import current_app

_client = None

def get_client():
    global _client
    if _client is None:
        mongo_uri = current_app.config.get("MONGO_URI")
        _client = MongoClient(mongo_uri)
    return _client


def get_db():
    client = get_client()
    return client["log_collector"]
