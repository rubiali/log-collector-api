from datetime import datetime
from app.schemas.log_schema import validate_log_payload, LogValidationError
from app.repositories.logs_repository import LogsRepository


class LogsService:
    def __init__(self):
        self.repository = LogsRepository()

    def _serialize_log(self, log: dict) -> dict:
        log["id"] = str(log.pop("_id"))
        return log

    def create_log(self, payload: dict) -> str:
        """
        Cria um novo log no sistema.
        """
        # Validação + normalização
        log_data = validate_log_payload(payload)

        # Persistência
        log_id = self.repository.insert_log(log_data)
        return log_id

    def get_logs(
        self,
        level: str | None = None,
        service: str | None = None,
        start_date: datetime | None = None,
        end_date: datetime | None = None
    ) -> list:
    
        """
        Busca logs aplicando filtros dinâmicos.
        """
        filters = {}

        if level:
            filters["level"] = level.upper()

        if service:
            filters["service"] = service

        if start_date or end_date:
            filters["created_at"] = {}

            if start_date:
                filters["created_at"]["$gte"] = start_date

            if end_date:
                filters["created_at"]["$lte"] = end_date

        logs = self.repository.find_logs(filters)
        return [self._serialize_log(log) for log in logs]
