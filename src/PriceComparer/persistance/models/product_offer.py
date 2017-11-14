from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import UUID

from PriceComparer.persistance.models.base_entity import DeclarativeBase


class ProductOffer(DeclarativeBase):
    """Sqlalchemy product offer model"""
    __tablename__ = "product_offers"

    id = Column(Integer, primary_key=True)
    search_id = Column('search_id', UUID, nullable=True)
    name = Column('name', String)
    product_code = Column('product_code', String, nullable=True)
    url = Column('url', String)
    retailer = Column('retailer', String)
    discounted_price = Column('discounted_price', Numeric, nullable=True)
    price = Column('price', Numeric, nullable=True)
    time = Column('created_at', DateTime, nullable=True)
