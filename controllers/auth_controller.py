# controllers/auth_controller.py
from flask import Blueprint, request, jsonify
from config.database import get_db_session
from services.auth_service import AuthService

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    """POST /register -> { email, password, role(optional) }"""
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "user")

    if not email or not password:
        return jsonify({"error": "email y password son obligatorios"}), 400

    # Se asume que AuthService.register_user devuelve el user o None si ya existe
    with get_db_session() as db:
        svc = AuthService(db)
        user = svc.register_user(email, password, role)
        if user is None:
            return jsonify({"error": "El correo ya está registrado"}), 409

        return jsonify({"id": user.id, "email": user.email, "role": user.role}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """POST /login -> { email, password }  devuelve { token }"""
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "email y password son requeridos"}), 400

    with get_db_session() as db:
        svc = AuthService(db)
        token = svc.login_user(email, password)   # se espera que devuelva token o None
        if not token:
            return jsonify({"error": "Credenciales inválidas"}), 401

        return jsonify({"message": "Login exitoso", "token": token}), 200
