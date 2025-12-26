from flask import Blueprint, request, jsonify, current_app
from datetime import datetime

from app.services.logs_service import LogsService
from app.schemas.log_schema import LogValidationError
from werkzeug.exceptions import BadRequest

logs_bp = Blueprint("logs_bp", __name__, url_prefix="/logs")


@logs_bp.route("", methods=["POST"])
def create_log():
    service = LogsService()

    try:
        payload = request.get_json(force=True)
        log_id = service.create_log(payload)

        return jsonify({
            "message": "Log criado com sucesso",
            "id": log_id
        }), 201

    except BadRequest:
        return jsonify({
            "error": "JSON inválido ou malformado"
        }), 400

    except LogValidationError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        current_app.logger.exception(e)
        return jsonify({
            "error": "Erro interno ao criar log"
        }), 500

@logs_bp.route("", methods=["GET"])
def get_logs():
    service = LogsService()
    try:
        level = request.args.get("level")
        service_name = request.args.get("service")

        start_date = request.args.get("from")
        end_date = request.args.get("to")

        start_date = (
            datetime.fromisoformat(start_date)
            if start_date else None
        )
        end_date = (
            datetime.fromisoformat(end_date)
            if end_date else None
        )

        logs = service.get_logs(
            level=level,
            service=service_name,
            start_date=start_date,
            end_date=end_date
        )

        return jsonify(logs), 200

    except ValueError:
        return jsonify({"error": "Formato de data inválido. Use ISO 8601."}), 400

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Erro interno ao buscar logs"}), 500
