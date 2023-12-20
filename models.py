import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

BASE = declarative_base()

class Publisher (BASE):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True, nullable=False)


class Book (BASE):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=100), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='book')

    

class Stock (BASE):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False) 
    book = relationship(Book, backref='stock')



class Sale (BASE):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric, nullable=False)  
    date_sale = sq.Column(sq.DateTime, nullable=False) 
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)    
    count = sq.Column(sq.Integer, nullable=False) 
    stock = relationship(Stock, backref='sale')

    

class Shop (BASE):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), nullable=False)


def create_tables(engine):
    BASE.metadata.drop_all(engine)
    BASE.metadata.create_all(engine)     
 