import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import DSN, Publisher, Book, Shop, Stock, Sale


engine = create_engine(DSN)

session = sessionmaker(bind=engine)
s = session()

file_json = '/home/roman/Документы/pythonProject/sql-homeworks-6/fixtures/tests_data.json'
with open(file_json, 'r') as f:
    templates = json.load(f)

for row in templates:
    print(row)
    if row['model'] == 'publisher':
        publisher = Publisher(id_publisher=row['pk'], name=row['fields']['name'])
        s.add(publisher)
        s.commit()
    if row['model'] == 'book':
        book = Book(id_book=row['pk'],
                    title=row['fields']['title'],
                    id_publisher=row['fields']['id_publisher'])
        s.add(book)
        s.commit()
    if row['model'] == 'shop':
        shop = Shop(id_shop=row['pk'], name=row['fields']['name'])
        s.add(shop)
        s.commit()
    if row['model'] == 'stock':
        stock = Stock(id_stock=row['pk'],
                      id_book=row['fields']['id_book'],
                      id_shop=row['fields']['id_shop'],
                      count=row['fields']['count'])
        s.add(stock)
        s.commit()
    if row['model'] == 'sale':
        sale = Sale(id_sale=row['pk'],
                    price=row['fields']['price'],
                    date_sale=row['fields']['date_sale'],
                    id_stock=row['fields']['id_stock'],
                    count=row['fields']['count'])
        s.add(sale)
        s.commit()


publisher = input('Какого издателя найти? ')
for Publisher.name in s.query(Publisher.id_publisher, Publisher.name).filter(Publisher.name == publisher):
    print(Publisher.name)


