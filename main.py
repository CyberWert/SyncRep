from sqlalchemy import create_engine
def fun100():
    eng = create_engine('sqlite:///baseAL.db')
    print('Database created')
    #eng.execute('dfdf')


fun100()