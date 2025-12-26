from pymongo.collection import Collection
from app.db.mongo import get_db


class LogsRepository:
    def __init__(self):
        db = get_db()
        self.collection: Collection = db["logs"]

    def insert_log(self, log_data: dict) -> str:
        """
        Insere um log no MongoDB.
        Retorna o ID do documento inserido.
        """
        result = self.collection.insert_one(log_data)
        return str(result.inserted_id)

    def find_logs(self, filters: dict) -> list:
        """
        Busca logs no MongoDB com filtros dinâmicos.
        """
        cursor = self.collection.find(filters).sort("created_at", -1)
        return list(cursor)
