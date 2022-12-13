
import copy


#TODO:fix ce problème
def part1(path):
    file = open(path)
    data = file.read().splitlines()
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
                if ord(charEncours) - ord(data[i][j+1])<2:
                    voisins.append(str(i)+"_" +str(j+1))
            grid[str(i)+"_"+str(j)]={"voisins":voisins,"distanceArrivee":-1}
    i=0
    voisins=grid[posArrivee]['voisins']
    grid[posArrivee]["distanceArrivee"]=0
    while grid[posDepart]["distanceArrivee"]==-1 and i<len(grid):
        #print(list(map(distArrivee,grid.values())))
        i=i+1
        voisinsProchainTour=[]
        if(len(voisins)>0):
            print(voisins)
        for voisinCeTour in voisins:
            if grid[voisinCeTour]["distanceArrivee"]==-1:
                grid[voisinCeTour]["distanceArrivee"]=i
                for v in grid[voisinCeTour]['voisins']:
                    voisinsProchainTour.append(v)
        voisins=voisinsProchainTour
    voisDepart=grid[posArrivee]['voisins']
    for v in voisDepart:
        print(grid[v]['distanceArrivee'])
    
    return grid[posDepart]["distanceArrivee"]



#print(part1("day12.txt"))


def part2(path):
    file = open(path)
    data = file.read().splitlines()
    grid = {}
    positionsDepart=[]
    posArrivee=""
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=="E":
                posArrivee=str(i)+"_"+str(j)
                data[i]=data[i].replace("E","z")
            if data[i][j]=="a":
                positionsDepart.append(str(i)+"_"+str(j))
            if data[i][j]=="S":
                data[i]=data[i].replace("S","a")
                positionsDepart.append(str(i)+"_"+str(j))
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
                if ord(charEncours) - ord(data[i][j+1])<2:
                    voisins.append(str(i)+"_" +str(j+1))
            grid[str(i)+"_"+str(j)]={"voisins":voisins,"distanceArrivee":-1}
    copieGrid=copy.deepcopy(grid)
    resultatDepuisDeparts=[]
    for posDepart in positionsDepart:
        grid=copy.deepcopy(copieGrid)
        i=0
        voisins=grid[posArrivee]['voisins']
        grid[posArrivee]["distanceArrivee"]=0
        while grid[posDepart]["distanceArrivee"]==-1 and i<len(grid):
            #print(list(map(distArrivee,grid.values())))
            i=i+1
            voisinsProchainTour=[]
            for voisinCeTour in voisins:
                if grid[voisinCeTour]["distanceArrivee"]==-1:
                    grid[voisinCeTour]["distanceArrivee"]=i
                    for v in grid[voisinCeTour]['voisins']:
                        voisinsProchainTour.append(v)
            voisins=voisinsProchainTour
        print(grid[posDepart]["distanceArrivee"])
        if grid[posDepart]["distanceArrivee"]!=-1:
            resultatDepuisDeparts.append(grid[posDepart]["distanceArrivee"])
    
    return min(resultatDepuisDeparts)




print(part2("day12.txt"))