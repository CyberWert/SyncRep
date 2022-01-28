def tasks():
    ls = [x ** y for x in range(2, 5) for y in range(9)]
    print(ls)
    ls2 = [[2, 3, 6], [5, 6, 7], [3, 8, 0]]
    ls3 = [j for i in ls2 for j in i]
    di2 = {'Key2': 45, 'DSD': 234}
    di3 = [di2[k] for k in di2]
    ls4 = [[x + y for x in 'ABCD'] for y in '1234']
    ls5 = [j for i in ls4 for j in i]
    ls6 = [[str(x) + str(y) for x in range(10) if x - y > 0] for y in range(10)]

    print(ls6)


tasks()
