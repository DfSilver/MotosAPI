from flask import Blueprint, request, jsonify
from config.database import get_db_session
from services.auth_service import AuthService

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    POST /register
    Crea un nuevo usuario con contraseña encriptada.
    Body JSON:
      {
        "email": "user@example.com",
        "password": "123456",
        "role": "admin" (opcional)
      }
    """
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "user")

    if not email or not password:
        return jsonify({"error": "email y password son obligatorios"}), 400

    with get_db_session() as db:
        svc = AuthService(db)
        user = svc.register_user(email, password, role)
        if user is None:
            return jsonify({"error": "El correo ya está registrado"}), 409

        return jsonify({
            "id": user.id,
            "email": user.email,
            "role": user.role
        }), 201
