import math
from builtins import print
from datetime import datetime


def haversine(lat1, lon1, lat2, lon2):

    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
         math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c

result = []
line = input("").split(",")
RADIUS = input("")
RADIUS = float(RADIUS)
LAT = float(line[0])
LOG = float(line[1])
title = input("")
temp = 1
temp =input()

temp = input().split(",")
date = datetime.strptime(temp[0], '%m/%d/%Y %H:%M')
lat = float(temp[1])
log = float(temp[2])
phone = temp[3]
x = haversine(LAT, LOG, lat, log)
if x <= RADIUS:
    result.append([date, lat, log, phone, x])


for i in range(len(result)):
    for j in range(1+i, len(result)):
        if result[i][3] == result[j][3]:
            if result[i][0] < result[j][0]:
                result.remove(result[i])
                break
            else:
                result.remove(result[j])
                break

result.sort(key=lambda result: result[3])
for i in range(len(result)-1):
    print(result[i][3], end=',')
print(result[len(result)-1][3])


