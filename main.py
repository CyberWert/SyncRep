import csv

def fun70():
    with open("./files/7lesson/CSVfile.csv", mode='w') as fl:
        wr = csv.DictWriter(fl, fieldnames=['First', 'Second', 'ffdf'], restval=100)
        wr.writerow({'First': 45, 'Second': 567})
        wr.writeheader()
        #wr.writerow(['456','677', '554'])
        #wr.writerow([5] * 3)
    with open("./files/7lesson/CSVfile.csv", mode='r') as fl:
        #rr = csv.reader(fl)
        rr = csv.DictReader(fl, fieldnames=['First', 'Second'], restkey='Reserved', restval='Empty')
        for i in rr:
            print(i)

import json
def fun701():
    """
    json
    """
    d = {'name': 'ffdf', 'phones': [6786567, 5671234]}
    print(d)
    json.dumps(d)

import json
def fun71(path, fljs, flcsv):
    """
    1)	Дан путь к json файлу и путь для файла с результатом. В JSON файле лежит лист диктов.
    Создать csv файл, колонками которого будут все существующие в JSON ключи, а значения - их значения из JSON.
    Если какого-то ключа в словаре нет - оставить в csv колонке пустое значение.
    Формат: str, str -> ...
    """
    di3 = {}
    #namein = input('Vvedite name:')
    namein = 'Mikhail Petrovich'
    try:
        if namein.isdigit():
            raise TypeError
    except TypeError:
        namein = input('Name must be a string. Vvedite name:')
    di = [{'Name1': namein, 'Age1': 17}, {'Name2': 'Fedor', 'Age2': 67}, {'Name3': 'Filip', 'Age3': 28}]
    with open(path+fljs, 'w') as flwr:
        json.dump(di, flwr)
    with open(path+fljs, 'r') as flrd:
        di2 = json.load(flrd)
    # print(di.keys())
    # for i in di.keys():
    #     print(f'True: {i}') if i is 'Name' else print(i)
    #print(di2)
    st = []
    stval = []
    for i in di2:
        ditmp = dict(i)
        for t, k in ditmp.items():
            st.append(t)
            stval.append(k)
    #print(st)
    with open(path+flcsv, 'w') as flrdcsv:
            wr = csv.writer(flrdcsv)
            #print(ditmp.keys())
            #wr = csv.DictWriter(flrdcsv, fieldnames=st)
            #wr.writeheader()
            wr.writerow(st)
            wr.writerow(stval)
    #with open(path+flcsv, 'r') as flrdcsv:
        #wr = csv.DictReader(flrdcsv, di3)
    #print(di3)


import os
def fun72(path, flexl, fljson):
    """
2)	Дан путь к excel таблице и путь для сохранения JSON. На каждой строке в первой ячейке имя, на второй - фамилия студента,
а затем в некотором количестве колонок идет по одной оценке (у каждого студента количество колонок может быть разным).
После завершения оценок в следующем столбце будет слово “end”. В последующих столбцах уже ничего не будет.
Объединить ячейки с именем и фамилией, а внутри вставить имя и фамилию, разделенные пробелом.
Перед именами и фамилиями вставить новый столбец, в котором будет прописана формула для вычисления среднего балла каждого студента.
Также в JSON файл, путь которого пришел в функцию задания, сохранить словарь следующего вида для всех студентов из таблицы:
    """
    import pandas as pd
    #os.chdir(r'C:\Users\admin\PycharmProjects\SyncProject\files\7lesson')
    #print(os.getcwd())
    #xl = pd.ExcelFile(path+flexl)
    xl1 = pd.read_excel(path+flexl)
    rez = list(zip(xl1["Имя"].tolist(), xl1['Фамилия'].tolist()))
    for i in rez:
        rez = ' '.join(i)
        print(rez)
    print(xl1)

#fun71('./files/7lesson/', 'JSONfile.json', 'CSVfile.csv')
fun72('./files/7lesson/', '2EXlfile.xlsx', '2JSONlife.json')