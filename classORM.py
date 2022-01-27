from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
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
Base = declarative_base()

class Shops(Base):
    __tablename__ = 'Shops'

    id_shop = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100))
    staff_amount = Column(Integer)

    def __int__(self, id_shop, name, address, staff_amount):
        self.id_shop = id_shop
        self.name = name
        self.address = address
        self.staff_amount = staff_amount

class Departments(Base):
    __tablename__ = 'Departments'

    id_dep = Column(Integer, primary_key=True)
    sphere = Column(String(50))
    staff_amount = Column(Integer)
    shop = Column(Integer, ForeignKey(Shops.id_shop))

    def __int__(self, sphere, staff_amount, shop):
        self.sphere = sphere
        self.staff_amount = staff_amount
        self.shop = shop

class Items(Base):
    __tablename__ = 'Items'

    id_item = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    description = Column(String(100), nullable=False)
    price = Column(Integer)
    department = Column(Integer, ForeignKey(Departments.id_dep))

    def __int__(self, name, description, price, department):
        self.name = name
        self.description = description
        self.price = price
        self.department = department

engine = create_engine('sqlite:///baseALC.db', echo=False)
Base.metadata.create_all(engine)

def create_tables():
    session = sessionmaker(bind=engine)
    ses = session()