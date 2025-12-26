from pymongo.collection import Collection
from app.db.mongo import get_db


class LogsRepository:
    def __init__(self):
        db = get_db()
        self.collection: Collection = db["logs"]