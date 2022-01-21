
class ABC(object):
    def __init__(self, a):
        self.a = a
    def cl_get(self):
        print(self.a)
    def cl_set(self, num):
        self.a = num

def fun80():
    cl = ABC(67)
    cl.cl_set(56)
    cl.cl_get()
    #root.pri(8)

def fun81():
    """
1)	Описать такую систему наследований классов Task1A, Task1B, Task1C, Task1D, Task1E без повторений переменных, чтобы:
a)	Переменная x со значением 1 доступна (но прописана только у одного) у классов Task1B и Task1C.
b)	Переменная x = 2 перегружена в классе Task1A (то есть она была бы 1, если бы не написали x = 2).
c)	В Task1D прописана переменная x = 3.
d)	Task1C наследуется от Task1D (не факт, что только от него)
e)	Task1A не наследуется от Task1C.
f)	В Task1E не прописан x, но доступен со значением 3. Наследуется только от одного родителя.
    """
    class Task1B(object):
        x = 1
        def __init__(self, x):
            self.x = x
        def set(self, num):
            self.x = num
        def get(self):
            return self.x
    class Tast1A(Task1B):
        def __init__(self, a):
            self.text = 'Class A'
            self.x = a
            pass
    class Task1D(Task1B):
        def __init__(self):
            self.x = 78
    class Task1C(Task1D):
            pass
    class Task1E(Task1B):
            pass

    bcl = Task1B(1)
    ccl = Task1C()
    acl = Tast1A(6)
    dcl = Task1D()
    ecl = Task1E(3)
    print(f'{bcl.x}, {ccl.x}, ({acl.x} + {acl.text}), {ecl.x}')

from decimal import Decimal
def fun82():
    """
2)	Описать класс Student (в корне файла), который на инициализацию принимает имя, фамилию и словарь оценок студента (сохранить в name, surname, marks).
Также во время инициализации сохраните в self.full_name одной строкой имя и фамилию, разделенные пробелом.
В словаре ключ - названия предметов, а значения - листы оценок (int). Описать у класса три метода:
    """
    class Student(object):
        name = str
        surname = str
        marks = {}
        full_name = str

        def __init__(self, n, s, m):
            self.name = n
            self.surname = s
            self.marks = m
            self.full_name = n + ' ' + s

        def check_subject(self, subject):
            for k in self.marks:
                if (subject == k or subject == None):
                    return True
            try:
                raise ValueError
            except ValueError:
                print("Incorrect subject. Program closed.")
                return False

        def get_aver_mark(self, subject=None):
            """
            a)	get_average_mark(subject=None)
            Вернуть средний балл студента (decimal). Если указано название предмета - то только по этому предмету.
            Если не указано - по всем предметам в целом (средний балл от всех средних баллов по предметам).
            Если указано несуществующее название предмета - вызвать ValueError.
            :param subject: предмет
            :return:
            """
            s1 = 0
            l1 = 0
            if subject == None:
                for k, v in self.marks.items():
                    s1 += sum(v)
                    l1 += len(v)
                    subject = 'All subjects'
            for k, v in self.marks.items():
                if subject == k:
                    s1 = sum(v)
                    l1 = len(v)
                        #print(f'Average for {k}={s}')
            frez = Decimal(s1)/Decimal(l1)
            return frez.quantize(Decimal('1.000'))
            #print(f'{subject}: {frez.quantize(Decimal("1.0000"))}')

        #@property

        def getSubjects(self):
            """
            b)	subjects - property, который возвращает лист всех предметов (исходя из данных с оценками).
            """
            spis = []
            for i in self.marks:
                spis.append(i)
            return spis
        def setST(self, x):
            self.marks = x
        def delST(self):
            del self.marks
        v = property(getSubjects, setST, delST, 'Property')

        def change_mark(self, subject, position, value):
            """
            c)	change_mark(subject, position, value)
            Заменяет у студента оценку по предмету subject с индексом position в массиве, устанавливая новое значение value.
            Если такого предмета нет - ValueError. Если индекс за пределами массива питон сам вызовет IndexError.
            """
            for k, v in self.marks.items():
                if subject == k:
                    v[position] = value
                    self.marks[k] = v
                    print(self.marks)
            return

        @staticmethod
        def compare_students(stud1, stud2, subject=None):
            """"
            d)	compare_students(student_1, student_2, subject=None)
            Сравнивает двух студентов по успеваемости и возвращает номер лучшего (1 или 2). Если средние баллы равны - вернуть 0.
            Если указан предмет (subject), то только по этому предмету, если не указан - по всем в целом. Используйте ранее описанный метод, вызвав его у объектов студентов!
            Если указано несуществующее название предмета - добиться ValueError.
            Метод должен быть статическим, так как тут нет необходимости в доступе к cls или self - у нас есть сами объекты студентов.
            """
            if stud1.check_subject(subject) and stud2.check_subject(subject):
                return (st.full_name, st.get_aver_mark(subject)) if st.get_aver_mark(subject) > st2.get_aver_mark(subject) else (st2.full_name, st2.get_aver_mark())
            else:
                return 0

    st = Student('Pavel', 'Pokarat', {'math': [8,8,4], 'lang': [5,2,7]})
    st2 = Student('Misha', 'Terpiloid', {'math': [2,3,1], 'lang': [9,8,6]})
    subj ='math'
    subj2 = 'lang'
    #print(subj)
    if st.check_subject(subj):
        st.get_aver_mark(subj)
    if st.check_subject(subj2):
        st.change_mark(subj2, 0, 2)
    print(Student.compare_students(st, st2, 'math'))
        #print(f'Studet1 in "{subj2}" average={st.get_aver_mark(subj2)}') if st.get_aver_mark(subj2) > st2.get_aver_mark(subj2) else print(f'Studet2 in "{subj2}" average={st2.get_aver_mark(subj2)}')
    #st.subjects()
    # print(st.v) #get
    # st.v = ['ddd'] #set
    # print(st.v)
    # del st.v #del
    # print(st.v)
        #print(st.full_name)

def fun83():
    """
    3)	Описать класс для игры в крестики-нолики TicTacToe. Инициализация объекта принимает два имени игроков (self.name_1 и self.name_2)
    и создает новое поле для игры 3 x 3 (проще всего создать лист из трех листов по 3 элемента - двумерный массив - быстро его можно создать генератором листов:
    """
    from random import randint
    class TTT():
        name1 = str
        name2 = str
        map = [[None] * 3 for i in range(3)]
        #pl = ra
        player = bool(randint(0,1))
        pl1_symb = 'X'
        pl2_symb = 'O'
        finished = False
#
        def next_move(self, row, column):
            if self.finished == True:
                return
            if self.map[row, column] == None:
                self.map[row, column] = self.player
            else:
                try:
                    raise IndexError
                except IndexError:
                    print('Поле занято')
        # def create_field (self):
        #     self.field
    a = TTT
    print(a.map, a.player)

def fun811():
    #x = 42 / (4 + 2 * (-2))
    #y = 1.2345e-3
    #y = 2014.0 ** 14
    y = 7 // 3
    y = 9 ** 19 - int(float(9 ** 19))
    print(y)

# def extfun(fun):
#     import time
#     print('extfun')
#     #print('calcfun')
#     s = time.time()
#     fun()
#     e = time.time()
#     print(e-s)

#@extfun
# def test():
#     r = 56 ** 245
#     print(r, "test fun")
#
# s = test()
# extfun(test())

# def decorator(func):
#     return 'sumit'
#
# @decorator
# def hello_world():
#     print('hello world')
#
# hello_world()

fun83()