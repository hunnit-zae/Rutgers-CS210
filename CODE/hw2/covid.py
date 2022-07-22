import csv
import math

file = open("covidTrain.csv","r")
reader=csv.reader(file)
covidTrain=[]
for line in reader:
    covidTrain.append(line)
file.close()

longitude=dict()
latitude=dict()
provinces = dict()
symptoms = dict()

for row in covidTrain [1:]:
    age = row[1]
    if '-' in str (age):
        i = age.find('-')
        avg = round((int(age[:i]) + int(age[i+1:])) / 2)
        row[1] = avg

    for i in range(8,11):
        date = row[i]
        row[i] = date[3:5] + '.' + date[0:2] + '.' + date[6:]

    Province = row[4]
    latt = float(row[6])
    long = float(row[7])

    if  not math.isnan(latt) and Province in latitude:
        latitude[Province] = (latitude[Province][0] + latt, latitude[Province][1] + 1)

    if not math.isnan(long) and Province in longitude:
        longitude[Province] = (longitude[Province][0] + long, longitude[Province][1] + 1)

    if Province not in latitude:
        latitude[Province] = (0,0)

    if Province not in longitude:
        longitude[Province] = (0,0)


for i in latitude.keys():
    latitude[i] = round(latitude[i][0] / latitude[i][1] ,2)

for i in longitude.keys():
    longitude[i] = round(longitude[i][0] / longitude[i][1], 2)  


for row in covidTrain [1:]:
    sym = row[11]
    Province = row[4]
    latt = float(row[6])
    long = float(row[7])
    City = row[3]

    if sym != 'NaN':
        newsym = sym.split(';')
        for item in newsym:
            item = item.strip()
            if Province in symptoms:
                if item in symptoms[Province]:
                    symptoms [Province][item] += 1
                else:
                    symptoms [Province][item ]= 1
            else:
                symptoms[Province] = dict()

    if City != 'NaN':
        if Province in provinces:
            if City in provinces[Province]:
                provinces [Province][City] += 1
            else:
                provinces [Province][City] = 1
        else:
            provinces [Province] = dict()

    if math.isnan(long):
        row[7] = longitude[Province]

    if math.isnan(latt):
        row[6] = latitude[Province]

for i in provinces:
    prov = provinces[i]
    provinces[i] ={k: v for k, v in sorted(prov.items(), key = lambda item: item[1])}

for row in covidTrain [1:]:
    Province = row[4]
    sym = row[11]
    m = -1
    n = ''
    if sym == 'NaN':
        symprov = symptoms[Province]
        for x in symprov:
            if symprov[x] > m:                
                m = symprov[x]
                n = x
            elif symprov[x] == m and x < n:
                m = symprov[x]
                n = x
        row[11] = n

for row in covidTrain[1:]:
    Province = row[4]
    City = row[3]
    m = -1
    n = ''
    
    if City == 'NaN':
        provprov = provinces[Province]
        for x in provprov:
            if provprov[x] > m:                
                m = provprov[x]
                n = x
            elif provprov[x] == m and x < n:
                m = provprov[x]
                n = x
        row[3] = n

for row in covidTrain [1:]:
    row[6] = round(float(row[6]),2)
    row[7] = round(float(row[7]),2)

with open('covidResult.csv','w') as f:
    for row in covidTrain:
        s = ''
        for i in row:
            s += str(i)+','
        f.write(s)
        f.write('\n')
f.close()