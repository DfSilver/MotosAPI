import jwt
import os
from functools import wraps
from flask import request, jsonify

SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key_123")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # El token puede venir en el encabezado Authorization
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"error": "Token faltante"}), 401

        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = decoded  # Guardamos info del usuario en el request
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401

        return f(*args, **kwargs)
    return decorated

def role_required(required_roles):
    """
    Verifica que el usuario tenga uno de los roles requeridos.
    Ejemplo de uso:
      @token_required
      @role_required(["admin"])
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = getattr(request, "user", None)
            if not user or "role" not in user:
                return jsonify({"error": "Token inválido o sin rol"}), 403

            if user["role"] not in required_roles:
                return jsonify({"error": "No tienes permiso para acceder a esta ruta"}), 403

            return f(*args, **kwargs)
        return wrapper
    return decorator

