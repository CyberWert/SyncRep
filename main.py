import csv

def fun70():
    with open("./files/7lesson/CSVfile.csv", mode='w') as fl:
        wr = csv.DictWriter(fl, fieldnames=['First', 'Second', 'ffdf'], restval=100)
        wr.writerow({'First': 45, 'Second': 567})
        wr.writeheader()
        #wr.writerow(['456','677', '554'])
        #wr.writerow([5] * 3)
    with open("./files/7lesson/CSVfile.csv", mode='r') as fl:
        #rr = csv.reader(fl)
        rr = csv.DictReader(fl, fieldnames=['First', 'Second'], restkey='Reserved', restval='Empty')
        for i in rr:
            print(i)

import json
def fun701():
    """
    json
    """
    d = {'name': 'ffdf', 'phones': [6786567, 5671234]}
    print(d)
    json.dumps(d)

fun701()