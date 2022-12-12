
import copy

def poids(case):
    if case['dejaVisite']:
        return 1
    return 0

def calculerMin(grid,posEncours, minActuel):
    gridMaj= copy.deepcopy(grid)
    nbVisite=sum(list(map(poids,grid.values())))
    resultats=[minActuel]
    if grid[posEncours]['estArrivee']==True:
        #print(grid[posEncours]['estArrivee'])
        #print(grid)
        return nbVisite
    else:
        gridMaj[posEncours]['dejaVisite']=True
        for voisin in grid[posEncours]['voisins']:
            if grid[voisin]['dejaVisite']==False and nbVisite+1<minActuel:
                minVoisin=calculerMin(gridMaj,voisin,minActuel)
                resultats.append(minVoisin) 
                minActuel=min(minActuel,minVoisin)    
    return min(resultats)

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
                if ord(charEncours) - ord(data[1][j]) < 2:
                    voisins.append(str(1)+"_" +str(j))
            if j == 0:
                if ord(charEncours) - ord(data[i][1])<2:
                    voisins.append(str(i)+"_" +str(1))
            if i == len(data)-1:
                if ord(charEncours) - ord(data[i-1][j])<2:
                    voisins.append(str(i-1)+"_" +str(j))
            if j == len(data[0])-1:
                if ord(charEncours) -ord(data[i][j-1])<2:
                    voisins.append(str(i)+"_" +str(j-1))
            if i != 0 and i !=len(data)-1 :
                if ord(charEncours)  - ord(data[i-1][j])<2:
                    voisins.append(str(i-1)+"_" +str(j))
                if ord(charEncours)  - ord(data[i+1][j]) <2:
                    voisins.append(str(i+1)+"_" +str(j))
            if j != 0 and j != len(data[0])-1:
                if ord(charEncours)  - ord(data[i][j-1])<2:
                    voisins.append(str(i)+"_" +str(j-1))
                if ord(charEncours)  - ord(data[i][j+1])<2:
                    voisins.append(str(i)+"_" +str(j+1))
            grid[str(i)+"_"+str(j)]={"voisins":voisins,"dejaVisite":False,"char":charEncours,"estArrivee":False}
    grid[posArrivee]["estArrivee"]=True
    return grid,posDepart






def part1(path):
    file = open(path)
    data = file.read().splitlines()
    grid,posDepart=creerGridAvecVoisins(data)
    return(calculerMin(grid,posDepart, len(data)*len(data[0])))


print(part1("test_day12.txt"))