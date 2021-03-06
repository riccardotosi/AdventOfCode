from collections import defaultdict # defualtdict never raises a KeyError; it provides a default value for the key that does not exists
from numpy import sign

def getHydrothermalVentsNoDiag(dict_data, line):
    start, end = line.split("->")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    x1 = int(x1) ; x2 = int(x2) ; y1 = int(y1) ; y2 = int(y2)
    if x1 == x2: # vertical hydrothermal vent
        ymin = min(y1,y2) ; ymax = max(y1,y2)
        for y in range (ymin, ymax+1):
            dict_data[(x1,y)] += 1
    elif y1 == y2: # horizontal hydrothermal vent
        xmin = min(x1,x2) ; xmax = max(x1,x2)
        for x in range (xmin, xmax+1):
            dict_data[(x,y1)] += 1
    else: # diagonal hydrothermal vent
        pass
    return dict_data

def getHydrothermalVentsWithDiag(dict_data, line):
    start, end = line.split("->")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    x1 = int(x1) ; x2 = int(x2) ; y1 = int(y1) ; y2 = int(y2)
    if x1 == x2: # vertical hydrothermal vent
        ymin = min(y1,y2) ; ymax = max(y1,y2)
        for y in range (ymin, ymax+1):
            dict_data[(x1,y)] += 1
    elif y1 == y2: # horizontal hydrothermal vent
        xmin = min(x1,x2) ; xmax = max(x1,x2)
        for x in range (xmin, xmax+1):
            dict_data[(x,y1)] += 1
    else: # diagonal hydrothermal vent
        y = y1 ; x = x1
        while y != y2 and x != x2:
            dict_data[(x,y)] += 1
            y += sign(y2-y1)*1
            x += sign(x2-x1)*1
        dict_data[(x,y)] += 1
    return dict_data

data = open('input.dat', 'r').read().splitlines()
dict_data_pt1 = defaultdict(lambda: 0) # function returning the default value for the dictionary defined

for line in data:
    dict_data_pt1 = getHydrothermalVentsNoDiag(dict_data_pt1, line)
overlaps = 0
for key, value in dict_data_pt1.items():
    if value >= 2:
        overlaps += 1
print("Number of points where at least two lines overlap:", overlaps)

dict_data_pt2 = defaultdict(lambda: 0) # function returning the default value for the dictionary defined
for line in data:
    dict_data_pt2 = getHydrothermalVentsWithDiag(dict_data_pt2, line)
overlaps = 0
for key, value in dict_data_pt2.items():
    if value >= 2:
        overlaps += 1
print("Number of points where at least two lines overlap:", overlaps)
