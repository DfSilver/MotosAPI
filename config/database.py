import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Importar Base del modelo de motocicletas
from models.motorcycle_model import Base

logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno desde .env
load_dotenv()

MYSQL_URI = os.getenv("MYSQL_URI")  # opcional
SQLITE_URI = "sqlite:///motorcycles_local.db"  # BD local por defecto


def get_engine():
    """
    Intenta crear una conexión con MySQL si MYSQL_URI está presente.
    Si falla o no existe, usa SQLite local.
    """
    if MYSQL_URI:
        try:
            engine = create_engine(MYSQL_URI, echo=True)
            conn = engine.connect()
            conn.close()
            logging.info("Conexión a MySQL exitosa.")
            return engine
        except OperationalError:
            logging.warning("No se pudo conectar a MySQL. Usando SQLite local.")

    engine = create_engine(SQLITE_URI, echo=True)
    logging.info("Conectado a SQLite en motorcycles_local.db")
    return engine


# Engine y sesión globales del módulo
engine = get_engine()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Crear tablas si no existen
Base.metadata.create_all(engine)


def get_db_session():
    """
    Retorna una nueva sesión de base de datos para ser utilizada
    en servicios o controladores.
    """
    return SessionLocal()

