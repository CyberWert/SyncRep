
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
    #x = 42 / (4 + 2 * (-2))
    #y = 1.2345e-3
    #y = 2014.0 ** 14
    y = 7 // 3
    y = 9 ** 19 - int(float(9 ** 19))
    print(y)
fun81()