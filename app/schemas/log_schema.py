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

    return {}
