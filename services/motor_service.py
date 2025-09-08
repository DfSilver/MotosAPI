from repositories.motor_repository import MotorRepository
from sqlalchemy.orm import Session

class MotorService:
    def __init__(self, db_session: Session):
        self.repo = MotorRepository(db_session)

    # ----------- Brands -----------
    def list_brands(self):
        return self.repo.get_all_brands()

    def get_brand(self, brand_id: int):
        return self.repo.get_brand_by_id(brand_id)

    def create_brand(self, name: str):
        return self.repo.create_brand(name)

    def delete_brand(self, brand_id: int):
        return self.repo.delete_brand(brand_id)

    # ----------- Motorcycles -----------
    def list_motorcycles(self):
        return self.repo.get_all_motorcycles()

    def get_motorcycle(self, motorcycle_id: int):
        return self.repo.get_motorcycle_by_id(motorcycle_id)

    def create_motorcycle(self, model: str, brand_id: int):
        return self.repo.create_motorcycle(model, brand_id)

    def delete_motorcycle(self, motorcycle_id: int):
        return self.repo.delete_motorcycle(motorcycle_id)
