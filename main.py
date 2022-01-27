#https://www.youtube.com/watch?v=sIbzKA6MId8
import sqlalchemy
from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey, and_
def fun100():
    meta = MetaData()
    eng = create_engine('sqlite:///baseAL.db', echo=False)
    print('Database created')
    table1 = Table('Tablica', meta,
                  Column('Number', Integer, primary_key=True),
                  Column('BookName', String(50), nullable=True)
                  )
    #print(table.primary_key)
    meta.create_all(eng)
    con = eng.connect()
    inc = table1.insert().values(BookName='tex1t')
    inc2 = table1.insert().values(BookName='333tedsxt2')
    #con.execute(inc)
    #con.execute(inc2)
    #print(sqlalchemy.__version__)
    #eng.execute('dfdf')
    reqse = table1.delete().where(table1.c.Number == 20)
    res = con.execute(reqse)
    reqse = table1.update().where(table1.c.Number == 24).values(BookName='Changed')
    res = con.execute(reqse)
    reqse = table1.select().where(table1.c.Number)
    res = con.execute(reqse)
    for i in res:
        print(i)
    #reqse = table1.drop()

from sqlalchemy.orm import mapper, sessionmaker, relationship, declarative_base
from classORM import Base, Shops, Departments, Items
def fun101(path):
    meta = MetaData()
    engine = create_engine(path, echo=False)
    session = sessionmaker(bind=engine)
    ses = session()
    si = Shops(name='Auchan', address='', staff_amount=250)
    ses.add(si)
    si = Shops(name='IKEA', address='Lynkir', staff_amount=500)
    ses.add(si)
    #ses.commit()
    ses.add_all([Departments(sphere='Furniture', staff_amount=250, shop=1),
                 Departments(sphere='Furniture', staff_amount=300, shop=2),
                 Departments(sphere='Dishes', staff_amount=200, shop=2)
                ])
    #ses.commit()
    ses.add_all([Items(name='Table', description='Cheap wooden table', price=300, department=1),
               Items(name='Table', description='', price=300, department=1),
               Items(name='Bed', description='Amazing wooden bed', price=300, department=1),
               Items(name='Cup', description='', price=300, department=1),
               Items(name='Plate', description='Glass plate', price=300, department=1)
              ])
    #ses.commit()
    qu = ses.query(Shops).filter(Shops.staff_amount > 100).filter(Shops.address == 'newaddress2')
    #qu = ses.query().delete('Shops')
    for i in qu:
        #print(i.name, i.address, i.staff_amount)
        if i != []:
            i.address = 'newaddress2'
            #ses.add(i)
            #ses.commit()
        print(i.name, i.address, i.staff_amount)
    # if i.address == 250:

fun101('sqlite:///baseALC.db')