#https://www.youtube.com/watch?v=sIbzKA6MId8
import sqlalchemy
from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey, and_
from sqlalchemy.orm import mapper, sessionmaker, relationship, declarative_base
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

def fun101():
    pass

fun101()