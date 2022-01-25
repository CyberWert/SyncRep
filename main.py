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

        @staticmethod
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
        def insert_values(con):
            curs = con.cursor()
            curs.execute('INSERT INTO Shops (id, name, address, staff_amount) VALUES (1, "Auchan", Null, 250);')
            curs.execute('INSERT INTO Shops (id, name, address, staff_amount) VALUES (2, "IKEA", "Zvezda 9", 500);')
            curs.execute('INSERT INTO Departments (id, sphere, staff_amount, shop) VALUES (1, "Furniture", 250, 1);')
            curs.execute('INSERT INTO Departments (id, sphere, staff_amount, shop) VALUES (2, "Furniture", 300, 2);')
            curs.execute('INSERT INTO Departments (id, sphere, staff_amount, shop) VALUES (3, "Dishes", 200, 2);')
            curs.execute('INSERT INTO Items (id, name, description, price, department) VALUES (1, "Table", "Cheap wooden", 300, 1);')
            curs.execute('INSERT INTO Items (id, name, description, price, department) VALUES (2, "Table", NULL, 750, 2);')
            curs.execute('INSERT INTO Items (id, name, description, price, department) VALUES (3, "Bed", "Amazing wooden bed", 1200, 2);')
            curs.execute('INSERT INTO Items (id, name, description, price, department) VALUES (4, "Cup", NULL, 10, 3);')
            curs.execute('INSERT INTO Items (id, name, description, price, department) VALUES (5, "Plate", "Glass plate", 20, 3);')
            #curs.execute('select * from Items;')
            # for i in curs:
            #     print(i)
            print('Tables inserted')

        @staticmethod
        def compare(con):
            """
            3)	Получаем в функцию task_3 путь к базе sqlite. Вернуть кортеж ответов на каждый запрос:
            Для сбора только уникальных значений пишем в самом начале SELECT DISTINCT
            """
            curs = con.cursor()
            print('a)	Получить все поля по товарам, у которых есть описание.')
            curs.execute('SELECT * FROM Items WHERE description NOT NULL;')
            for i in curs:
                print(i)
            print('b)	Получить все направления отделов, в которых более 200 сотрудников. Избегать повторений.')
            curs.execute('SELECT DISTINCT sphere FROM Departments WHERE staff_amount;')
            print(curs.fetchmany(7))
            print('c)	Получить все адреса магазинов с названием, начинающихся на английскую букву “I”. Использовать LIKE (см. файл “Дополнительно).')
            curs.execute('SELECT name FROM Shops WHERE name LIKE "I%";')
            print(curs.fetchone())
            print('d)	Получить все названия товаров, которые продаются в отделах с мебелью (sphere == Furniture).')
            curs.execute('SELECT name FROM Items WHERE department IN '
                         '(SELECT id FROM Departments WHERE sphere == "Furniture");')
            print(curs.fetchall())
            print(' e)	Получить названия магазинов, где в продаже есть товары с описанием.')
            curs.execute('SELECT description FROM Items WHERE description NOT Null;')
            print('Description NULL: ', curs.fetchall())
            curs.execute('SELECT shop FROM Departments WHERE id IN '
                         '(SELECT department FROM Items WHERE description NOT Null);')
            print('Departments with description NULL: ', curs.fetchall())
            curs.execute('SELECT name FROM Shops WHERE id IN '
                         '(SELECT shop FROM Departments WHERE id IN '
                         '(SELECT department FROM Items WHERE description NOT Null));')
            print(curs.fetchall())
            print('f)	Получить для каждого товара все его поля (кроме id) + все поля его отдела (кроме id), '
                        'причем для всех полей отдела в ответе должна быть приписка department_{название_поля} + все поля его магазина (кроме id)'
                        ' с припиской shop_{название_поля}.')
            curs.execute('SELECT name, description, price, department FROM Items;')
            for i in curs:
                print(i)

        @staticmethod
        def sqldel4(con):
            """
            4)	Получаем в функцию task_4 путь к базе sqlite. Удалить все товары, у которых цена больше 500 и у которых нет описания.
            """
            curs = con.cursor()
            curs.execute('DELETE FROM Items WHERE price > 500 AND description IS NULL')
            #con.commit()
            s1 = 'SELECT * FROM Items'
            curs.execute(s1)
            print(curs.fetchall())
            #curs.execute(';')

        @staticmethod
        def sqldel5(con):
            """
            5)	Получаем в функцию task_5 путь к базе sqlite. Удалить все товары, у которых магазин не имеет адреса.
            """
            curs = con.cursor()
            curs.execute('SELECT * FROM Items;')
            s1 = '(SELECT id FROM Shops WHERE address IS NULL))'
            s2 = '(SELECT id FROM Departments WHERE shop IN '
            s3 = 'DELETE FROM Items WHERE department IN '
            curs.execute(s3+s2+s1)
            #curs.execute('DELETE FROM Items WHERE department IN (SELECT id FROM Departments WHERE shop IN (SELECT id FROM Shops WHERE address IS NULL))')
            curs.execute('SELECT * FROM Items;')
            print(curs.fetchall())

    con = Sqwork.connect()
    Sqwork.add_tables(con)
    Sqwork.insert_values(con)
    #Sqwork.compare(con)
    Sqwork.sqldel5(con)
    con.close()


#fun90()
fun91('base91.sql')