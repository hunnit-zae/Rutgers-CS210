import csv
import math
from collections import Counter
from collections import defaultdict

file = open("pokemonTrain.csv","r")
reader=csv.reader(file)
pokemon=[]


for line in reader:
    pokemon.append(line)
file.close()

firetype = 0
firetypeover40=0

for row in pokemon:
    if row [4]=="fire":
        firetype +=1
        if float (row[2]) >= 40:
            firetypeover40 += 1
percentage = round(firetypeover40 / firetype * 100)
with open("pokemon1.txt", "w") as f:
    f.write("Percentage of fire type Pokemons at or above level 40 = "+ str(percentage))


weakness=dict()
for row in pokemon[1:]:
    type = row [4]
    weak = row [5]
    if weak not in weakness:
        weakness [weak]=[]

    if type != "NaN":
        weakness [weak].append(type)

 
def findType(lst: list) -> str:
    typecount = Counter(lst)
    type = ""
    cnt = 0
    for key, val in typecount.items():
        if val > cnt or (key < type and val == cnt):
               type = key  
    return type

for key in weakness:
    weakness[key] = findType(weakness[key])

for row in pokemon:
    if row[4] == "NaN":
        row[4] = weakness[row[5]]

atkover40=[]
Defover40=[]
HPover40=[]
atkunder=[]
Defunder=[]
HPunder=[]
totalhp=0
stage_3=0

for row in pokemon[1:]:
    level=float (row[2])
    atk=float (row[6])
    Def=float (row[7])
    HP=float (row[8])
    stage=float (row[9])
    if level >40:
        if not math.isnan(atk):
            atkover40.append(atk)
        if not math.isnan(Def):
            Defover40.append(Def)
        if not math.isnan(HP):
            HPover40.append(HP)
    else:
        if not math.isnan(atk):
            atkunder.append(atk)
        if not math.isnan(Def):
            Defunder.append(Def)
        if not math.isnan(HP):
            HPunder.append(HP)
    if stage==3:
        totalhp+=HP
        stage_3+=1

avgatk = round(sum(atkover40) / len(atkover40), 1)
avgDef = round(sum(Defover40) / len(Defover40), 1)
avgHP = round(sum(HPover40) / len(HPover40), 1)
avgatkunder = round(sum(atkunder) / len(atkunder), 1)
avgDefunder = round(sum(Defunder) / len(Defunder), 1)
avgHPunder = round(sum(HPunder) / len(HPunder), 1)

for row in pokemon[1:]:
    level = float(row[2])
    if row[6] == "NaN":
        if level > 40:
            row[6]=avgatk
        else: 
            row[6]=avgatkunder

    if row[7] == "NaN":
        if level > 40:
            row[7]=avgDef
        else:
            row[7]=avgDefunder
            
    if row[8] == "NaN":
        if level > 40:
            row[8]=avgHP
        else:
            row[8]=avgHPunder
            
file = open("pokemonResult.csv","w")
writer=csv.writer(file)
writer.writerows(pokemon)
file.close()

plty=defaultdict(list)
for row in pokemon[1:]:
    type = row[4]
    p = row[3]
    if p not in plty[type]:
        plty[type].append(p)
for t in plty:
    plty[t].sort()

result = sorted(list(plty))

with open("pokemon4.txt", "w") as f:
    f.write("Pokemon type to personality mapping: ")
    f.write("\n")
    for t in result:   
        a = ", ".join(plty[t])
        f.write(f" {t}: {a}\n")


totalHP = 0.0
stage_3 = 0
for row in pokemon[1:]:
    if float(row[9]) == 3.0:
        totalHP += float(row[8])
        stage_3 = stage_3 + 1
avgHP = round(totalHP / stage_3)
with open("pokemon5.txt", "w") as f:
    f.write("Average hit point for Pokemons of stage 3.0 = " + str(avgHP))