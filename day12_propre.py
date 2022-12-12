
import copy

def poids(case):
    if case['dejaVisite']:
        return 1
    return 0


def distanceALarrive(grid,pos):
    posVoisins=grid[pos]['voisins']
    distancesParVoisin=[len(grid.keys())]
    gridMaj= copy.deepcopy(grid)
    gridMaj[pos]['dejaVisite']=True
    for posVoisin in posVoisins:
        if not gridMaj[posVoisin]['dejaVisite']:
            if grid[posVoisin]['distanceArrivee']!=0:
                print("coucou")
                distancesParVoisin.append(grid[posVoisin]['distanceArrivee']+1)
            else:
                if grid[posVoisin]['estArrivee']==True:
                    distancesParVoisin.append(1)
                else:
                    distancesParVoisin.append(distanceALarrive(gridMaj,posVoisin)+1)
    gridMaj[pos]['distanceArrivee']=min(distancesParVoisin)
    print(grid)
    return min(distancesParVoisin)

#TODO:fix ce problème
def creerGridAvecVoisins(data):
    grid = {}
    posDepart=""
    posArrivee=""
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=="E":
                posArrivee=str(i)+"_"+str(j)
                data[i]=data[i].replace("E","z")
            if data[i][j]=="S":
                posDepart=str(i)+"_"+str(j)
                data[i]=data[i].replace("S","a")
    for i in range(len(data)):
        for j in range(len(data[i])):
            charEncours=data[i][j]
            voisins = []
            if i == 0:
                if abs(ord(charEncours) - ord(data[1][j]) )< 2:
                    voisins.append(str(1)+"_" +str(j))
            if j == 0:
                if abs(ord(charEncours) - ord(data[i][1]))<2:
                    voisins.append(str(i)+"_" +str(1))
            if i == len(data)-1:
                if abs(ord(charEncours) - ord(data[i-1][j]))<2:
                    voisins.append(str(i-1)+"_" +str(j))
            if j == len(data[0])-1:
                if abs(ord(charEncours) -ord(data[i][j-1]))<2:
                    voisins.append(str(i)+"_" +str(j-1))
            if i != 0 and i !=len(data)-1 :
                if abs(ord(charEncours)  - ord(data[i-1][j]))<2:
                    voisins.append(str(i-1)+"_" +str(j))
                if abs(ord(charEncours)  - ord(data[i+1][j])) <2:
                    voisins.append(str(i+1)+"_" +str(j))
            if j != 0 and j != len(data[0])-1:
                if abs(ord(charEncours)  - ord(data[i][j-1]))<2:
                    voisins.append(str(i)+"_" +str(j-1))
                if abs(ord(charEncours)  - ord(data[i][j+1]))<2:
                    voisins.append(str(i)+"_" +str(j+1))
            grid[str(i)+"_"+str(j)]={"voisins":voisins,"dejaVisite":False,"char":charEncours,"estArrivee":False,"distanceArrivee":-1}
    i=0
    voisins=grid[posArrivee]['voisins']
    grid[posArrivee]["distanceArrivee"]=0
    while grid[posDepart]["distanceArrivee"]==-1:
        print(grid[posDepart]["distanceArrivee"])
        i=i+1
        voisinsProchainTour=[]
        for voisin in voisins:
            if grid[voisin]["distanceArrivee"]==-1:
                grid[voisin]["distanceArrivee"]=i
                for v in grid[voisin]['voisins']:
                    voisinsProchainTour.append(v)
        voisins=voisinsProchainTour
    return grid[posDepart]["distanceArrivee"]


def part1(path):
    file = open(path)
    data = file.read().splitlines()
    return(creerGridAvecVoisins(data))


print(part1("day12.txt"))