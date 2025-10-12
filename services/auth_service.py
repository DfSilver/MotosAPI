import bcrypt
from models.user_model import User

class AuthService:
    def __init__(self, db_session):
        self.db = db_session

    def register_user(self, email, password, role="user"):
        # Verificar si el correo ya existe
        existing = self.db.query(User).filter(User.email == email).first()
        if existing:
            return None

        # Encriptar contraseña
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Crear usuario nuevo
        user = User(email=email, password=hashed.decode("utf-8"), role=role)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
