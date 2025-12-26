from datetime import datetime


class LogValidationError(Exception):
    """Erro lançado quando o payload do log é inválido."""
    pass


def validate_log_payload(data: dict) -> dict:
    """
    Valida o payload recebido para criação de um log.

    Campos obrigatórios:
    - level (str)
    - service (str)
    - message (str)

    Campos opcionais:
    - metadata (dict)

    Retorna o payload normalizado.
    """

    if not isinstance(data, dict):
        raise LogValidationError("Payload deve ser um objeto JSON")

    # Campos obrigatórios
    required_fields = ["level", "service", "message"]

    for field in required_fields:
        if field not in data:
            raise LogValidationError(f"Campo obrigatório ausente: {field}")

        if not isinstance(data[field], str) or not data[field].strip():
            raise LogValidationError(f"Campo '{field}' deve ser uma string não vazia")

    # Normalização
    normalized_log = {
        "level": data["level"].upper(),
        "service": data["service"],
        "message": data["message"],
        "created_at": datetime.utcnow()
    }

    return normalized_log
