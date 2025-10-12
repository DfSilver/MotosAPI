from sqlalchemy.orm import Session
from repositories.motorcycle_repository import MotorcycleRepository

class MotorcycleService:
    """
    Capa de servicios para la lógica de negocio de motocicletas.
    """

    def __init__(self, db_session: Session):
        self.repository = MotorcycleRepository(db_session)

    def listar_motos(self):
        return self.repository.get_all()

    def obtener_moto(self, moto_id: int):
        return self.repository.get_by_id(moto_id)

    def crear_moto(self, brand: str, reference: str):
        return self.repository.create(brand, reference)

    def actualizar_moto(self, moto_id: int, brand: str | None = None, reference: str | None = None):
        return self.repository.update(moto_id, brand, reference)

    def eliminar_moto(self, moto_id: int):
        return self.repository.delete(moto_id)
