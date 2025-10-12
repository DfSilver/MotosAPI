from sqlalchemy import Column, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    role = Column(String(50), default="user")  # Puede ser 'user' o 'admin'

    def __repr__(self):
        return f"<User(email={self.email}, role={self.role})>"
