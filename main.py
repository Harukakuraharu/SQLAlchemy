import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import json
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from datetime import datetime

load_dotenv() 

password_DB = os.getenv('PASSWORD_DB')
name_DB = os.getenv('NAME_DB')
login_DB = os.getenv('LOGIN_DB')
driver = os.getenv('DRIVER')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

DSN = f'{driver}://{login_DB}:{password_DB}@{db_host}:{db_port}/{name_DB}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r') as f:
    data = json.load(f)

# print(data)
for record in data:
    # print(record)
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


parametrs = input()
filtered = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name.ilike(parametrs))
for title, name, price, date_sale in filtered.all():
    
    print(f"{title} | {name} | {price} | {datetime.date(date_sale).strftime('%d-%m-%Y')}")


session.close()