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
fun601()