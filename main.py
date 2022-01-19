
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

fun80()