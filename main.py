import random
import sys

def fun60():
    """

    """
    str = 'Я волна'
    stren = str.encode("cp1251")
    print(stren)
    strb = stren
    for i in strb:
        if i != 223:
            print(i, ascii(i))
    stren = stren.decode("utf-8", "replace")
    print(stren)
    print(sys.getdefaultencoding())
    (strb)
    # t = (6,5,9,0,6,0)
    # print(t.count(0))
    # print(type(t))

from random import randint
def fun601():
    """
    work with files
    """
    str2 = ''
    with open("./log.txt", mode="r+") as hand:
        str3 = hand.readlines()
        #hand.flush()
    #str = str[0:15]
    for i in range(len(str3)):
        if str3[i] !='x':
            str2 += str3[i]
            #print(str[i])
            #print(f'Empty: {str[i]}')
    #print(str[1].encode())
    i = randint(56, 678)
    print(f'I={i}')
    with open("./log.txt", mode="a") as hand:
        hand.writelines("New string " + str(i) + '\n')
    print(str3)
    print(len(str3))

#import file45
from datetime import datetime as dt
import sys

#def taskmain(a, b):
    #file45.tfun([45, 67, 56, 334])
    #print(dir(file40))
    #return (a+4*b)*(a-3*b)+a**2

    #taskmain(23,3)

def fun33():
    if sys.platform == "win32":
        #print("OS: {}, comment: {}, time {time}".format(sys.platform, 56, time=dt.today()))
        print(f"OS: {sys.platform}, comment {sys.version_info}")

def fun34():
    print(sys.getdefaultencoding())
    s = "пап а".encode()
    try:
        print(s.decode())
    except UnicodeDecodeError:
        print("Не правильная кодировка")
        s = s.decode('cp1251')
    else:
        print("Декодировка прошла успешно")
    finally:
        print(f"Результат: {s}")

def fun35():
    fl = open("./log.txt", mode='r+t')
    #print(fl.readlines())
    fl.write("Zxcxczxc xczxcc22\n")
    #print(fl.readline())
    fl.flush()
    fl.close()

def fun36():
    # with open('log2.txt', mode='a+') as fl2:
    #     fl2.write("fdsssd dsdfsdf 45\n")
    # fl2.close()
    with open('log2.txt', mode='r+') as fl3:
        print(fl3.read(7))
        fl3.seek(12)
        print(fl3.read())
        #for item in fl3:
    #print(fl3.read() + "ee")

#6.1 home регулярные выражения
import re
def fun61a():
    """
1)	В файле “task1_input.txt” находится текст.
a)	Найти в тексте все слова, которые начинаются с большой английской буквы, затем идут только маленькие (только буквы английского алфавита).
Длина слова должна быть не менее 3 символов и не более 10 символов. Перед словом должен быть пробел или начало строки.
Слово должно заканчиваться пробелом, запятой, двоеточием, точкой с запятой, точкой или концом строки. Lookahead и lookbehind assertion в помощь.
Также флаг MULTILINE может быть некоторым полезен :)
Записать в текстовый файл “task1_output.txt” строку:
“Слова: …” (слова, разделенные запятыми с пробелом)
    """
    #str = input("Slovo")
    regex = r'[a-Z]'
    with open('./files/6lesson/in61a.txt', mode='r+') as fl4:
        filestr = fl4.readline()
        print(f'String: {filestr}')
        #res3 = re.match(regex, filestr)
    #res3 = re.match('\W{1}', filestr)
    #print(res3.string)
    #res2 = re.findall('\w+@\w+\.\w{3}', filestr)
    reg = r'[A-Z][a-z]{3,9}[ ,:;\.\n]'
    res2 = re.findall(reg, filestr, flags=re.MULTILINE)
    #res2 = re.findall('[ |^][A-Z][a-z]{3,9}[ ,:;\.\n]', filestr, flags=re.MULTILINE)
    #res3 = re.sub(' ', '', res2)
    print(res2)
    with open('./files/6lesson/out61a.txt', mode='w+') as filout1:
        str1 = res2
        #print(str1)
        filout1.write('Words: ')
        for item in str1:
            filout1.write(item+', ')
        filout1.write('\n')

def fun61b():
    """
b)	Теперь найти в тексте все мобильные номера по Беларуси, исходя из того, что они начинаются на +375, а затем идет 9 цифр.
Номер может быть разделен знаками “-” или “ “. Возможные места разделения: +375-29-123-45-67. В других местах разделений быть не может.
Из самого номера нас интересует только код оператора и номер без разделителей.
То есть из такого номера: +37529-123-4567 нам нужно получить: 291234567. Перед плюсиком может быть что угодно.
После номера обязательно должен быть пробел, перенос строки или конец текста.
В сами группы собираем только нужные наборы цифр, а питоном уже соединяем группы в одну строку.
Дописать в task1_output.txt строку:
    """
    resli = list()
    with open('./files/6lesson/in61b.txt', mode='r+') as f8:
        text = f8.read()
        res = re.findall('375[- ]?\d{2}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}[-]?', text)
        print(f'Phone numbers: {res}')
        # print(res2)
        # print(f'Res3 = {res3}')
        for item in res:
            res2 = re.sub('[ -]', '', item)
            res3 = re.sub('375', '', res2)
            resli.append(res3)
        #print(resli)

    with open('./files/6lesson/out61b.txt', mode='a+') as f8out:
        f8out.write('\n' + 'Phones: ')
        for item in resli:
            f8out.write(item + ' ')

def fun611():
    """
    заменить каждое целое число (последовательность цифр) на его куб.
    """
    text = "Too many 0.56 numbers: 3.3 and 35 8 ds 3.1456 dfg 12234"
    regfl = r'(\d+\.\d+)'
    regint = r'([^\.]\d+)'
    regint2 = r'([^\.]?\d+[^\.])'
    rezfl = re.findall(regfl, text)
    rezint = re.findall(regint, text)
    print(rezfl, rezint)
    for i in rezfl:
        #i=int(i) if i.is_integer() else i=float(i)
        #print(type(i))
        tmp = float(i) ** 2
        text = text.replace(i, str(tmp))
        #rez2.append(tmp)
    for i in rezint:
        tmp = int(i) ** 2
        text = text.replace(i, str(tmp))
    #rez3 = re.sub(reg, rez2, text)
    print(text)

from os import walk
def fun61c(path):
    """
2)	Дан путь к папке (приходит в функцию). Необходимо собрать древовидную структуру о содержимом папки. Каждый уровень должен содержать ключи:
a)	FOLDERS - папки, где внутри будет аналогично описаны папки и файлы следующего уровня вложенности.
b)	FILES - словарь с именами файлов, где есть информация о размере файла и его формате.
Если файл текстовый (имя заканчивается на .txt, то еще указана его длина в символах).
    """
    di = {}
    di1 = {'DIR': {}, 'FOLDERS': {}, 'FILES': {}}
    dif = {}
    tar = str()
    dr = {}
    diformat = {}
    lsrez = list()
    rez = walk(path)
    for i in rez:
        #print(i)
        di1.update({'DIR': i[0], 'FOLDERS': i[1], 'FILES': i[2]})
        #print(i[1])
        #print(di1)
        for f in i[2]:
            print(f)
            #print(i.__sizeof__())
            tar = str(f).split('.')
            diformat = {"SIZE": f.__sizeof__(), "FORMAT": tar[1]}
            dif.update({f: diformat})
            #print(dif)
            if tar[1] == 'txt':
                for fold in i[1]:
                    print(fold)
                    with open("./files/" + str(fold) + '/' + f, mode="r+") as opfi:
                        simb = len(opfi.read())
                        print(simb)
                    #diformat.update({"LENGHT": simb})
                    #print(diformat)
    #                 #print(len(simb))
    #             #print(tar[1])
    #         #print(diformat)
    #         di.update({i: diformat})
    #         #print(di)
    #         dr.update({b: di})
    #     for j in b:
    #         #print(j)
    #         di1.update({j: di})
    # #print(dr)
        print(dif)


    #print(di.items())

#fun37()
def fun6112():
    str1 = "number 672-123-456-9910"
    reg = r'[\d-]+'
    rez = re.findall(reg, str1)
    print(rez)

fun61c("./files")

#d = dt.now()
#print(d,'\n',d.microsecond)
#print(dt.astimezone(dt.now()))

#print(task2_19({1: 5, 4: 3, 2: 2}))
#print(fl.task2_1("Съешь этих уебанских пельменей, выблядок"))
#ask = input("What is your name? ")
#print("User text:", ask)