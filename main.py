import sqlite3
import sqlite3 as sq3
from sqlite3 import Error
def fun90():
    try:
        con = sq3.connect('mybase.sql')
    except Error:
        print(Error)
    finally:
        print('Connected to base succesful')
    curs = con.cursor()
    curs.execute('CREATE TABLE Name (id int);')
    #print(curs.execute(table))

def fun91(path_base):
    """
1)	Функция task_1 принимает путь к sqlite базе данных, создать таблицы
Shops:
■	id - INTEGER PRIMARY
■	name - VARCHAR (название магазина)
■	address - VARCHAR NULLABLE (адрес магазина)
■	staff_amount - INTEGER (количество сотрудников)
Departments:
■	id - INTEGER PRIMARY
■	sphere - VARCHAR (направление работы отдела - например, одежда, игрушки, посуда и т.д.)
■	staff_amount - INTEGER (количество сотрудников)
■	shop - FOREIGN KEY на Shops.id (в каком магазине отдел)
Items:
■	id - INTEGER PRIMARY
■	name - VARCHAR (название товара)
■	description - TEXT NULLABLE (описание)
■	price - INTEGER (цена)
■	department - FOREIGN KEY на Department.id (в каком отделе продается)
"""
    class Sqwork:
        path2 = 'base91.sql'

        def connect():
            con = sqlite3.connect(path_base)
            print('Connected')
            return con

        @staticmethod
        def add_tables(con):
            curs = con.cursor()
            curs.execute('DROP TABLE Shops')
            curs.execute('DROP TABLE Departments')
            curs.execute('DROP TABLE Items')
            curs.execute('CREATE TABLE Shops (id int PRIMORY KEY, name varchar, address varchar, staff_amount int);')
            curs.execute('CREATE TABLE Departments (id int PRIMORY KEY, sphere varchar, staff_amount int, shop int, FOREIGN KEY (shop) references Shops(id));')
            curs.execute('CREATE TABLE Items(id int, name varchar, description text NULL, price int, department int, FOREIGN KEY (department) references Departments(id));')
            print('Tables added')
            curs.close()

        @staticmethod
        def insert_values():
            print('Tables inserted')
    con = Sqwork.connect()
    Sqwork.add_tables(con)
    Sqwork.insert_values()


#fun90()
fun91('base91.sql')