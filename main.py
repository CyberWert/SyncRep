def diffarray(ch, a, b):
    """
    #It should remove all values from list a, which are present in list b keeping their order.
    #array_diff([1,2],[1]) == [2]
    #If a value is present in b, all of its occurrences must be removed from the other:
    #array_diff([1,2,2,2,3],[2]) == [1,3]
    """
    if ch == 1:
        for i in a:
            for y in b:
                if i == y:
                    a.remove(i)
    elif ch == 2:
        a = set(a)
        a = list(a)
        print(a)
        for i in b:
            for j in a:
                if i == j:
                    a.remove(j)
    else:
        return
    return print(a)

#gens
#stroki()
#bubble([7,4,6,3,1])
#diffarray(2, [1,2,4,4,2,3,2,4,4,4,4,5,3],[2,3,4])

def new():
    """
    Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string.
    Note:
    Empty string values should be ignored.
    Empty arrays or null/nil/None values being passed into the method should result in an empty string being returned.
    ['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
    ['ninja', '', 'ronin'] --> "ninja and ronin"
    :return:
    """
    li = ['ninja', 'samurai', 'ronin']
    li2 = ' '.join(li)
    print(sorted(li))
    rez = li2.replace(' ', ' and ', 1)
    print(rez)


def descending_order(num):
    rez =[]
    rez2 = str
    tmp = str
    if isinstance(num, int):
        while num > 1:
            tmp = num % 10
            rez.append(int(tmp))
            num /= 10
            # rez = set(rez)
            # rez = list(rez)
            rez.sort(reverse=True)
            rez2 = [str(i) for i in rez]
            rez2 = ','.join(rez2)
            rez2 = rez2.replace(',', '')
    print(int(rez2))


#descending_order(468949493342)
#descending_order([5,2])


def abbr(name2):
    name2 = name2.title()
    name2 = name2.split(' ')
    name3 = str()
    name3 = [i[0] for i in name2]
    name3 = '.'.join(name3)
    # for i in name2:
    #     name3 = str(name3) + i[0]
    # name3 = '.'.join(name3)
    return print(name3)
    #return print('.'.join((i[0] for i in name2)).title())


#abbr('patrick feeney')


def alphabet_position(var):
    var = var.lower()
    num2 = [ord(i)-96 for i in var if 0 < (ord(i)-96) < 32]
    num3 = [str(i) for i in num2]
    str3 = ' '.join(num3)
    str3.capitalize()
    return print(str(str3))


#alphabet_position("The sunset sets at twelve o' clock.")

def to_jaden_case(str2):
    # str3 = str2[0].upper()
    # for i in range(1, len(str2)):
    #     if str2[i-1] == ' ' and i - 1 != None:
    #         #str2.replace(str2[i+1], ' ' + str2[i+1].upper())
    #         str3 += str2[i].upper()
    #         i = i + 1
    #     else:
    #         str3 += str2[i]
    print(str2.split('r'))
    str3 = ' '.join([i.capitalize() for i in str2.split()])
    print(str3)
    #return print(type(string), string.title())


#to_jaden_case("How can mirrors be real if our eyes aren't real")


def wordspath(val):
    str1 = val.split()
    di = {}
    ls = []
    for i in str1:
        for j in i:
            if j.isdigit():
                di[j] = i
    keylist = dict(sorted(di.items()))
    for k, v in keylist.items():
        ls.append(v)
    str1 = ' '.join(ls)
    print(str1)

#wordspath("Fo1r the2 g3ood 4of th5e pe6ople")
#wordspath("is2 Thi1s T4est 3a")


def get_sum(a, b):
    sum1 = 0
    str1 = str()
    if a < b:
        mi = a
        mx = b
    elif a > b:
        mx = a
        mi = b
    else:
        return 'since both are same'
    for i in range(mi, mx+1):
        str1 += str(i) + ' '
        sum1 += i
    #(-1, 2) --> 2(-1 + 0 + 1 + 2 = 2)
    #return f'({mi}, {mx}) --> {sum}({str1})= {sum})'
    #print(res)
    print(sum(range(min(a, b), max(a, b)+1)))
    """
    Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it.
    If the two numbers are equal return a or b.
    """

#get_sum(-1, 2)

def umbling (val):
    """
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"
    """
    str1 = str()
    ls = list()
    ls2 = list()
    for i in range(len(val)):
        str1 += str(val[i]).upper()
        str1 += val[i].lower() * i
        ls.append(str1)
        str1 = []
    for i in ls:
        str3 = ''.join(i)
        ls2.append(str3)
    val = '-'.join(ls2)
    #str2 = '-'.join(ls)
    return val


#umbling('ZpglnRxqenU')

from datetime import datetime, timedelta, time
def decorfun(fun):
    def wrapper():
        d = datetime.now()
        d2 = datetime
        print('Wrapper', d.microsecond)
        fun()
        d1 = datetime.now()
        print('After wrapper', d1.microsecond)
        #d2.time
        print((abs(d1.microsecond - d.microsecond) / 1000000).__round__(3))
    return wrapper

@decorfun
def fun1():
    print('fun1')
    x = 9876978 ** 45534

#fun1()

def pig_it(val):
    'Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.'
    # return ' '.join([w[1:] + w[0] + 'ay' if w.isalpha() else w for w in text.split(' ')])
    str3 = str()
    ls2 = list()
    for i in val.split():
        for j in range(1, len(i)):
            str3 += i[j]
        if i[0].isalpha():
            str3 += i[0] + 'ay'
        else:
            str3 += i[0]
        ls2.append(str3)
        str3 = str()
    str4 = ' '.join(ls2)
    print(str4)


#pig_it('O tempora o mores !') # igPay atinlay siay oolcay


def create_phone_number(val):
    """Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
    """
    #return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    print(val)
    #print(f'({val[0]}{val[1]}{val[2]}) {val[3]}{val[4]}{val[5]}-{val[6]}{val[7]}{val[8]}{val[9]}')
    print('({}{}{}) {}{}{}{}{}{}{}'.format(*val))
    #print(*val)

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])