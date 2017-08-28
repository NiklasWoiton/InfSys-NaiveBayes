import csv
from itertools import chain, product


# 0 1 3 4 6 Keep in changeOne aka keep Overall, value, room, cleanliness, service; drop location, fronst desk and buisness service
def changeData():
    rawData = csv.reader(open("rawData.csv", "rb"))
    changeOne = [tuple(line)[len(line) - 8:] for line in rawData]  # drops columns left of overall Rating
    changeTwo = [tuple(line)[:len(line) - 5] for line in changeOne]  # saves column 0 und 1
    changeThree = [tuple(line)[len(line) - 4:len(line) - 3:] for line in changeOne]  # saves column 3 and 4
    changeFour = [tuple(line)[len(line) - 2:len(line) - 1:] for line in changeOne]  # saves column 6
    writer = csv.writer(open("workData.csv", "wb"))
    for x in range(0, len(changeOne), 1):
        toDoRow = (changeTwo[x]+changeThree[x]+changeFour[x])
        writer.writerow(toDoRow)
        x += x






changeData()
