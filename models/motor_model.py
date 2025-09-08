from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    motorcycles = relationship('Motorcycle', back_populates='brand', cascade='all, delete-orphan')

class Motorcycle(Base):
    __tablename__ = 'motorcycles'
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String(255), nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship('Brand', back_populates='motorcycles')
