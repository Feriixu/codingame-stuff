import sys
import math

lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())

defibs = []
for i in range(n):
    defib = input().split(';')
    defib[4] = float(defib[4].replace(',', '.'))
    defib[5] = float(defib[5].replace(',', '.'))
    defibs.append(defib)

mindist = math.inf
mindefib = ""
for defib in defibs:
    defib_lon = defib[4]
    defib_lat = defib[5]

    x = (defib_lon - lon) * math.cos((lon + defib_lon/(2)))
    y = (defib_lat - lat)
    d = math.sqrt(x**2 + y**2) * 6371
    if d < mindist: 
        mindist = d
        mindefib = defib[1]

print(mindefib)