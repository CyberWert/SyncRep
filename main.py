"""
1)	Получаем число, некоторое количество аргументов (от 0) и некоторое количество именованных аргументов (от 0).
Сравнить число со всеми аргументами и именованными аргументами, а также их типы. 
Собрать результаты проверок для обычных аргументов в массив из кортежей bool [(значения_равны, типы_равны), ...]. 
Для именованных аргументов в словарь, где ключи - имя переменной, а значения - tuple из двух bool переменных (тоже значения_равны и типы_равны). 
Вернуть полученный лист и словарь.
Пример: 5, 6, 5.0, True, x = 5, y = ‘hi’ -> [(False, True), (True, False), (False, False)], {‘x’: (True, True), ‘y’: (False, False)}
Формат: int, args, kwargs -> list, dict

fdfdfdffdfs sdfsdf
"""

def fun51(num, *args, **kwargs):
    rez = [45,56]
    rez2 = list()
    dic1 = dict()
    for i in args:
        if num == i:
            rez[0]=True
        else:
            rez[0] = False
        if type(num) == type(i):
            rez[1]=True
        elif type(num) != type(i):
            rez[1]=False
        rez2.append(tuple(rez))
    for i,j in kwargs.items():
        #print(i,j)
        if num == j:
            r1 = True
        else:
            r1 = False
        if type(j) == type(num):
            r2 = True
        else:
            r2 = False
        dic1.update({i: (r1, r2)})
    #print(args, kwargs)
    print(rez2, ';', dic1)

fun51(35, 34, 56,35,45 "s", ind1=35, ind2="Petrov")