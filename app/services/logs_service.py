from datetime import datetime
from app.schemas.log_schema import validate_log_payload, LogValidationError
from app.repositories.logs_repository import LogsRepository


class LogsService:
    def __init__(self):
        self.repository = LogsRepository()

    def create_log(self, payload: dict) -> str:
        """
        Cria um novo log no sistema.
        """
        # Validação + normalização
        log_data = validate_log_payload(payload)

        # Persistência
        log_id = self.repository.insert_log(log_data)
        return log_id

    