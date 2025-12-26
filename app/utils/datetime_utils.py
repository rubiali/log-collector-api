from datetime import datetime


def parse_iso_date(date_str: str | None) -> datetime | None:
    """
    Converte string YYYY-MM-DD para datetime.
    Retorna None se vazio.
    """
    if not date_str:
        return None

    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Formato de data inválido. Use YYYY-MM-DD")
