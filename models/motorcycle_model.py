from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Motorcycle(Base):
    """
    Representa una motocicleta en el sistema.
    Atributos:
      - id: entero autoincrementable (PK)
      - brand: marca de la moto (p. ej., Yamaha, Honda)
      - reference: referencia/modelo (p. ej., MT-07, CB500F)
    """
    __tablename__ = "motorcycles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    brand = Column(String(100), nullable=False)
    reference = Column(String(150), nullable=False)
