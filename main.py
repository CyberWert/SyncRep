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
    print(strb)

fun60()