import csv
from itertools import chain, product


# 0 1 3 4 6 Keep in changeOne aka keep Overall, value, location. cleanliness, service; drop rooms, fronst desk and buisness service
def changeData():
    rawData = csv.reader(open("rawData.csv", "rb"))
    changeOne = [tuple(line)[len(line) - 8:] for line in rawData]  # drops columns left of overall Rating
    changeTwo = [tuple(line)[:len(line) - 6] for line in changeOne]  # speichert spalte 0 und 1
    print changeTwo[0]
    print changeTwo[2]
    changeThree = [tuple(line)[len(line) - 2:len(line) - 1:] for line in changeOne]
    print changeThree[0]
    print changeThree[2]
    changeFour = [tuple(line)[len(line) - 5:len(line) - 3:] for line in changeOne]
    print changeFour[0]
    print changeFour[2]
    # print dir(tuple)
   # print dir(list)

changeData()
