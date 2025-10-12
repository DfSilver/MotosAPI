from models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os

# Clave secreta (recomendado pasarla por .env)
SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key_123")

class AuthService:
    def __init__(self, db):
        self.db = db

    def register_user(self, email, password, role="user"):
        """
        Registra un nuevo usuario con contraseña encriptada.
        Si el correo ya existe, retorna None.
        """
        # Verificar si el usuario ya existe
        existing_user = self.db.query(User).filter_by(email=email).first()
        if existing_user:
            return None

        # Encriptar contraseña correctamente
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        # Crear y guardar nuevo usuario
        new_user = User(email=email, password=hashed_password, role=role)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user

    def login_user(self, email, password):
        """
        Valida credenciales y devuelve un token JWT si son correctas.
        """
        user = self.db.query(User).filter_by(email=email).first()

        # Verificar credenciales
        if not user or not check_password_hash(user.password, password):
            return None

        # Generar token JWT
        token_payload = {
            "id": user.id,
            "email": user.email,
            "role": user.role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(token_payload, SECRET_KEY, algorithm="HS256")
        return token
