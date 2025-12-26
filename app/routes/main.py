from flask import Blueprint, jsonify

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def hello_world():
    return {"message": "Hello World!"}