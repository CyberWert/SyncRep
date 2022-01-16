"""
1)	55555Получаем число, некоторое количество аргументов (от 0) и некоторое количество именованных аргументов (от 0).
Сравнить число со всеми аргументами и именованными аргументами, а также их типы. 
Собрать результаты проверок для обычных аргументов в массив из кортежей bool [(значения_равны, типы_равны), ...]. 
Для именованных аргументов в словарь, где ключи - имя переменной, а значения - tuple из двух bool переменных (тоже значения_равны и типы_равны). 
Вернуть полученный лист и словарь.
Пример: 5, 6, 5.0, True, x = 5, y = ‘hi’ -> [(False, True), (True, False), (False, False)], {‘x’: (True, True), ‘y’: (False, False)}
Формат: int, args, kwargs -> list, dict
from anoterh
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

def fun511(*args, ind):
    """
    task5_2-from work
    """
    #help(fun52)
    #print(sum(args))
    x, *y = range(5, 10, 2)
    print(x, y)
    filter(x != 2, range(3))

from functools import reduce
import re

def fun52(num):
    """
2)	Написать лямбда функции для нескольких целей. Сохранять их в переменные с указанными названиями в корне файла (будет импортирована в тесты).
a)	task_2_a (в массиве будут только числа формата int)
Функция для filter, задача которой отсеять все числа, которые делятся на 10 или нечетные или выходят за рамки диапазона от 0 до 100
(для проверки диапазона не использовать and - сделать в одной проверке с двухсторонними сравнениями).
b)	task_2_b (в массиве будут только числа формата int)
Функция для map, задача которой умножить все нечетные числа на 2, а все четные поделить на два (оставив в формате int).
Используйте тернарный оператор (читайте в “Дополнительно”):
c)	task_2_c (в массиве будут только строки)
Функция для reduce, которая вычисляет суммарное количество английских маленьких букв (a - z) во всех строках в массиве.
Третьим параметров в reduce будет передан 0 (начальное значение).
d)	task_2_d (в массиве будут только decimal)
Функция, принимающая массив decimal чисел, и отдающая среднее арифметическое всех положительных.
Формат: list -> decimal
    """
    print(num)
    sum = 0
    num2 = [2,3,5,18,45]
    num3 = ['sdAD', 'dfgR', 'SaS']
    re = (r'[a-z]')
    #print(re)
    def fun3c(x,y):
        for i in x+y:
            if i == 's':
                return i
    #f = (lambda num: num*4)
    task_2_a = filter((lambda x: 0 < x < 100 and x % 2 == 0 and x % 10 != 0), num)
    task_2_b = map((lambda x: x / 2 if x % 2 == 0 else x * 2), num)
    #task_2_c = reduce(fun3c, num2) #нужно from functools import reduce
    task_2_d = filter((lambda x: x > 0), num)
    for i in task_2_d:
        sum +=i
    #t = num / 2 if num % 2 == 0 else num * 2
    #print(task_2_c)
    #fun3c('sdAD', 'dfgR')
    #print(int(f))

from time import sleep
def fun53(is_slow):
    """
3)	Написать генератор (yield), который будет отдавать числа Фибоначчи (int):
0, 1, 1, 2, 3, 5, 8, 13, 21…
Генератор должен прекратить работу, если текущее число превысило 1 млрд. Тогда это число уже не отдавать.
Генератор назвать стандартным именем функции для текущего задания. Сам генератор принимает bool параметр для инициализации (is_slow, например).
 Если этот параметр = True, то ответ отдавать минимум через 0.5 секунд. Если же False или ничего не передали, то сразу же.
    """
    s = 1
    i1 = 0
    maxnum = 16
    ls = [0, 1]
    #rez = (i+i for i in range(1,6))
    if is_slow == True:
        print("Sleeping 0,5 sec")
        sleep(1)
        print("End sleeping")
    num = 0
    next1 = 1
    for i in range(1, maxnum):
        rez3 = num + next1
        num = next1
        next1 = rez3
        if rez3 > 500:
            print("Result > 500")
            break
        ls.append(rez3)
    print(ls)

    # for i in range(i1, maxnum):
    #     yield i
    # print(i)
    # if i < 100:
    #     print(rez2)
    # for j in range(1,5):
    #     print(j)

def fun533(fun):
    """
    Использование декоратора
    """
    return "Decor fun"

    @fun53
    def fun112():
        print("fun111")


fun53(1)
# for i in a:
#     print(i)
# print(type(a))
#fun52(*{4,5,6,7}, ind=5)
#fun51(35, 34, 56,35,45,"s", ind1=35, ind2="Petrov")