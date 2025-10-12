from sqlalchemy.orm import Session
from models.motorcycle_model import Motorcycle

class MotorcycleRepository:
    """
    Repositorio para CRUD de motocicletas.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    # CREATE
    def create(self, brand: str, reference: str) -> Motorcycle:
        moto = Motorcycle(brand=brand, reference=reference)
        self.db.add(moto)
        self.db.commit()
        self.db.refresh(moto)
        return moto

    # READ (list & get)
    def get_all(self) -> list[Motorcycle]:
        return self.db.query(Motorcycle).all()

    def get_by_id(self, moto_id: int) -> Motorcycle | None:
        return self.db.query(Motorcycle).filter(Motorcycle.id == moto_id).first()

    # UPDATE
    def update(self, moto_id: int, brand: str | None = None, reference: str | None = None) -> Motorcycle | None:
        moto = self.get_by_id(moto_id)
        if not moto:
            return None
        if brand is not None:
            moto.brand = brand
        if reference is not None:
            moto.reference = reference
        self.db.commit()
        self.db.refresh(moto)
        return moto

    # DELETE
    def delete(self, moto_id: int) -> Motorcycle | None:
        moto = self.get_by_id(moto_id)
        if not moto:
            return None
        self.db.delete(moto)
        self.db.commit()
        return moto
