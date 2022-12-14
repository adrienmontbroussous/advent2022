


def moveSand(rockList,xSand,ySand,ymaxRock,xMinRock,xMaxRock):
    newRockList=rockList
    newXSand=500
    nexYsand=0
    stop=False
    if ySand>=ymaxRock or xMinRock>xSand or xMaxRock<xSand:
        stop=True
    elif (str(xSand)+"_"+str(ySand+1)) not in rockList:
        #on descend
        newXSand=xSand
        nexYsand=ySand+1
    elif (str(xSand-1)+"_"+str(ySand+1)) not in rockList:
        #on va en bas à gauche
        newXSand=xSand-1
        nexYsand=ySand+1
    elif (str(xSand+1)+"_"+str(ySand+1)) not in rockList:
        #on va en bas à droite
        newXSand=xSand+1
        nexYsand=ySand+1
    else:
        newRockList.append(str(xSand)+"_"+str(ySand))

    return stop,newXSand,nexYsand,newRockList


def ajouterRocksEntre(debut, fin,rocks):
    first = [int(debut[0]), int(debut[1])]
    second = [int(fin[0]), int(fin[1])]
    if first[0] == second[0]:
        x = first[0]
        for y in range(min(first[1], second[1]), max(first[1], second[1])+1):
            rocks.add(str(x)+"_"+str(y))
    if first[1] == second[1]:
        y = first[1]
        for x in range(min(first[0], second[0]), max(first[0], second[0])+1):
            rocks.add(str(x)+"_"+str(y))
    return rocks
    


def part1(path):
    file = open(path)
    data = file.read().splitlines()
    grid = [[]for i in range(len(data))]
    rocks=set()
    xSand=500
    ySand=0
    maxYRock=0
    xMinRock=500
    xMaxRock=500
    for i in range(len(data)):
        temp=data[i].split(' -> ')
        for j in range(len(temp)):
            grid[i].append(temp[j].split(","))
    for chemin in grid:
        for j in range(len(chemin)-1):
            debut=chemin[j]
            fin=chemin[j+1]
            yDebut=debut[1]
            xDebut=debut[0]
            xFin=fin[0]
            yFin=fin[1]
            
            rocks=ajouterRocksEntre(debut,fin,rocks)
            maxYRock=max(max(int(maxYRock),int(yDebut)),int(yFin))
            xMinRock=min(min(int(xMinRock),int(xDebut)),int(xFin))
            xMaxRock=max(max(int(xMaxRock),int(xDebut)),int(xFin))
    rocks=list(set(rocks))
    lenRockListInit=len(rocks)
    print(lenRockListInit)
    stop=False
    while not stop:
        stop,xSand,ySand,rocks=moveSand(rocks,xSand,ySand,maxYRock,xMinRock,xMaxRock)
    rocks=list(set(rocks))
    resultat=len(rocks)-lenRockListInit
    return (resultat)

#print(part1("day14.txt"))

#1001

def moveSand2(rockList,xSand,ySand,ymaxRock,xMinRock,xMaxRock):
    newRockList=rockList
    newXSand=500
    nexYsand=0
    stop=False

    if (str(newXSand)+"_"+str(nexYsand)) in rockList:
        #on est à la source, on s'arrête
        stop=True
    elif(ySand==ymaxRock-1):
        #on est tout en bas, on s'arrête
        newRockList.append(str(xSand)+"_"+str(ySand))
    elif (str(xSand)+"_"+str(ySand+1)) not in rockList:
        #on descend
        newXSand=xSand
        nexYsand=ySand+1
    elif (str(xSand-1)+"_"+str(ySand+1)) not in rockList:
        #on va en bas à gauche
        newXSand=xSand-1
        nexYsand=ySand+1
    elif (str(xSand+1)+"_"+str(ySand+1)) not in rockList:
        #on va en bas à droite
        newXSand=xSand+1
        nexYsand=ySand+1
    else:
        newRockList.append(str(xSand)+"_"+str(ySand))
        print(len(rockList))

    return stop,newXSand,nexYsand,newRockList
#TODO:opti les perfs c'est loooong
def part2(path):
    file = open(path)
    data = file.read().splitlines()
    grid = [[]for i in range(len(data))]
    rocks=set()
    xSand=500
    ySand=0
    maxYRock=0
    xMinRock=500
    xMaxRock=500
    for i in range(len(data)):
        temp=data[i].split(' -> ')
        for j in range(len(temp)):
            grid[i].append(temp[j].split(","))
    for chemin in grid:
        for j in range(len(chemin)-1):
            debut=chemin[j]
            fin=chemin[j+1]
            yDebut=debut[1]
            xDebut=debut[0]
            xFin=fin[0]
            yFin=fin[1]
            
            rocks=ajouterRocksEntre(debut,fin,rocks)
            maxYRock=max(max(int(maxYRock),int(yDebut)),int(yFin))
            xMinRock=min(min(int(xMinRock),int(xDebut)),int(xFin))
            xMaxRock=max(max(int(xMaxRock),int(xDebut)),int(xFin))
    rocks=list(set(rocks))
    lenRockListInit=len(rocks)
    maxYRock=maxYRock+2
    stop=False
    while not stop:
        stop,xSand,ySand,rocks=moveSand2(rocks,xSand,ySand,maxYRock,xMinRock,xMaxRock)
    rocks=list(set(rocks))
    resultat=len(rocks)-lenRockListInit
    return (resultat)



print(part2("day14.txt"))
#27976