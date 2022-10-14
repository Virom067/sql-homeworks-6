from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, Float, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


DSN = f"postgresql://postgres:postgres@localhost:5432/sql_netology_db_hm_6"
engine = create_engine(DSN)

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id_publisher = Column(Integer, primary_key=True)
    name = Column(VARCHAR(250), nullable=False)


class Book(Base):
    __tablename__ = 'book'

    id_book = Column(Integer, primary_key=True)
    title = Column(VARCHAR(250), nullable=False)
    id_publisher = Column(Integer, ForeignKey("publisher.id_publisher"))
    Publisher = relationship("Publisher")


class Shop(Base):
    __tablename__ = 'shop'

    id_shop = Column(Integer, primary_key=True)
    name = Column(VARCHAR(250), nullable=False)


class Stock(Base):
    __tablename__ = 'stock'

    id_stock = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey("book.id_book"))
    id_shop = Column(Integer, ForeignKey("shop.id_shop"))
    count = Column(Integer, nullable=False)

class Sale(Base):
    __tablename__ = 'sale'

    id_sale = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    date_sale = Column(DATE, nullable=False)
    id_stock = Column(Integer, ForeignKey("stock.id_stock"))
    count = Column(Integer, nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

