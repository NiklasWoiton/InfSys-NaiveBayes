import csv
from itertools import chain, product


# 0 1 3 4 6 Keep in changeOne aka keep Overall, value, location. cleanliness, service; drop rooms, fronst desk and buisness service
def changeData():
    rawData = csv.reader(open("rawData.csv", "rb"))
    changeOne = [tuple(line)[len(line) - 8:] for line in rawData]  # drops columns left of overall Rating
    changeTwo = [tuple(line)[:len(line) - 6] for line in changeOne]  # saves column 0 und 1
    print changeTwo[0]
    print changeTwo[2]
    changeThree = [tuple(line)[len(line) - 5:len(line) - 3:] for line in changeOne]  # saves column 3 and 4
    print changeThree[0]
    print changeThree[2]
    changeFour = [tuple(line)[len(line) - 2:len(line) - 1:] for line in changeOne]  # saves column 6
    print changeFour[0]
    print changeFour[2]
    writer = csv.writer(open("workData.csv", "w"))
    for x in range(0, len(changeOne), 1):
        toDoRow = (changeTwo[x]+changeThree[x]+changeFour[x])
        # print toDoRow
        writer.writerow(toDoRow)
        x += x






changeData()
