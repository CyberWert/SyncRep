#https://www.youtube.com/watch?v=sIbzKA6MId8
import sqlalchemy
from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey, and_, or_
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
    # q = ses.query(Shops.name)
    # for i in q:
    #     print(q)
    #if not ses.query(Shops):
    # si = Shops(name='Auchan', address='', staff_amount=250)
    # ses.add(si)
    # si = Shops(name='IKEA', address='Lynkir', staff_amount=500)
    # ses.add(si)
    # ses.commit()
    # ses.add_all([Departments(sphere='Furniture', staff_amount=250, shop=1),
    #              Departments(sphere='Furniture', staff_amount=300, shop=2),
    #              Departments(sphere='Dishes', staff_amount=200, shop=2)
    #             ])
    # ses.commit()
    # ses.add_all([Items(name='Table', description='Cheap wooden table', price=300, department=1),
    #            Items(name='Table', description='', price=300, department=1),
    #            Items(name='Bed', description='Amazing wooden bed', price=300, department=1),
    #            Items(name='Cup', description='', price=300, department=1),
    #            Items(name='Plate', description='Glass plate', price=300, department=1)
    #           ])
    # ses.commit()
    # qu = ses.query(Shops).delete()
    # qu = ses.query(Departments).delete()
    # qu = ses.query(Items).delete()
    # ses.commit()
    qu = ses.query(Shops).filter(Shops.staff_amount > 100).filter(Shops.address == 'Lynkir')
    for i in qu:
        print(tuple([i.name, i.address, i.staff_amount]))
        # if i != []:
        #     print(i.name, i.address, i.staff_amount)
            #i.address = 'Lynkir'
            #ses.add(i)
            #ses.commit()
    # Вернуть лист товаров (объекты).
    qu = ses.query(Items).all()
    # for i in qu:
    #     print(i.department, i.name, i.description, i.price)
    # Вернуть кортежи товаров и их отделов.
    for i in ses.query(Departments).filter(Departments.sphere == 'Furniture'):
        print(i)
    #II-A. Вернуть идентификаторы 3 - 4 по счету товаров из выборки, отсортированной по имени товара.
    qu = ses.query(Items).order_by(Items.name).filter(or_(Items.id_item == 4, Items.id_item == 3))
    for i in qu:
        print(tuple([i.id_item, i.name]))
    print('----------')
    print("II-B. Выбрать названия товаров и названия их отделов, если и товар, и отдел существуют.")
    qu = ses.query(Items, Departments).filter(Items.name != None).filter(Items.department == Departments.id_dep).filter(Departments.id_dep != None)
    for row in qu:
        print(row)
    print('----------')
    print("3.	Вернуть лист адресов по списку объектов.")
    qu = ses.query(Shops.id_shop, Shops.address)
    for row in qu:
        print(row)
    print('----------')
    print("5.	Вернуть лист магазинов:")
    qu = ses.query(Shops)
    ls = []
    for row in qu:
        ls.append(row)
    print(ls)
    print('----------')
    print("6.	Вернуть кортежи вида (Товар, Отдел, Магазин) для каждого товара.")
    qu = ses.query(Items, Departments, Shops).filter(Items.department == Departments.id_dep).filter(Departments.shop == Shops.id_shop)
    for row in qu:
        print(row)

fun101('sqlite:///baseALC.db')