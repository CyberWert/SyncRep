import csv

def fun70():
    with open("./files/7lesson/CSVfile.csv", mode='w') as fl:
        wr = csv.writer(fl)
        wr.writerow(['456','677', '554'])
        wr.writerow([5,6,7])
    with open("./files/7lesson/CSVfile.csv", mode='r') as fl:
        rr = csv.reader(fl)
        for i in rr:
            print(i)

fun70()