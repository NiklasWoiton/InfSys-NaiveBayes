import csv
from itertools import chain, product


# 0 1 2 4 6 Keep in changeOne aka keep Overall, value, room, cleanliness, service; drop location, fronst desk and buisness service
def changeData():
    rawData = csv.reader(open("rawData.csv", "rb"))
    listData = [list(line)[len(line) - 8:] for line in rawData]  # drops columns left of Overall Rating
    relevantColumns = [0, 1, 2, 4, 6]
    relevantData = []
    for row in range(0, len(listData)):
        relevantData.append([])
        for column in range(0, len(relevantColumns)):
            relevantData[row].append(listData[row][relevantColumns[column]])
    relevantData[0] = tuple(['Gesamtbewertung', 'Qualitaet', 'Einrichtung', 'Kueche', 'Service'])
    writer = csv.writer(open("workData.csv", "wb"))
    [writer.writerow(tuple(relevantData[row])) for row in range(0, len(relevantData))]


changeData()
