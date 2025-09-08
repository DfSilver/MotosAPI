from models.motor_model import Brand, Motorcycle
from sqlalchemy.orm import Session

class MotorRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    # ----------- Brands -----------
    def get_all_brands(self):
        return self.db.query(Brand).all()

    def get_brand_by_id(self, brand_id: int):
        return self.db.query(Brand).filter(Brand.id == brand_id).first()

    def create_brand(self, name: str):
        brand = Brand(name=name)
        self.db.add(brand)
        self.db.commit()
        self.db.refresh(brand)
        return brand

    def delete_brand(self, brand_id: int):
        brand = self.get_brand_by_id(brand_id)
        if brand:
            self.db.delete(brand)
            self.db.commit()
        return brand

    # ----------- Motorcycles -----------
    def get_all_motorcycles(self):
        return self.db.query(Motorcycle).all()

    def get_motorcycle_by_id(self, motorcycle_id: int):
        return self.db.query(Motorcycle).filter(Motorcycle.id == motorcycle_id).first()

    def create_motorcycle(self, model: str, brand_id: int):
        moto = Motorcycle(model=model, brand_id=brand_id)
        self.db.add(moto)
        self.db.commit()
        self.db.refresh(moto)
        return moto

    def delete_motorcycle(self, motorcycle_id: int):
        moto = self.get_motorcycle_by_id(motorcycle_id)
        if moto:
            self.db.delete(moto)
            self.db.commit()
        return moto
