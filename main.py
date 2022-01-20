
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
a)	get_average_mark(subject=None)
Вернуть средний балл студента (decimal). Если указано название предмета - то только по этому предмету.
Если не указано - по всем предметам в целом (средний балл от всех средних баллов по предметам).
Если указано несуществующее название предмета - вызвать ValueError.
b)	subjects - property, который возвращает лист всех предметов (исходя из данных с оценками).
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
            print(f'{subject}: {frez.quantize(Decimal("1.0000"))}')

        #@property
        def subjects(self):
            spis = []
            for i in self.marks:
                spis.append(i)
            return print(spis)

    st = Student('Pavel', 'Pokarat', {'math': [8,8,4], 'lang': [5,2,7]})
    subj = None
    #print(subj)
    if st.check_subject(subj):
        st.get_aver_mark(subj)
    st.subjects()
        #print(st.full_name)

def fun811():
    #x = 42 / (4 + 2 * (-2))
    #y = 1.2345e-3
    #y = 2014.0 ** 14
    y = 7 // 3
    y = 9 ** 19 - int(float(9 ** 19))
    print(y)
fun82()