import csv

def fun70():
    with open("./files/7lesson/CSV.csv", mode='r') as fl:
        wr = csv.writer(fl)
        wr.writerow(['456','677',554])
    print()
