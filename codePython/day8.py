

def part1(path):
    file = open(path)
    data = file.read().splitlines()
    indicesArbresVisibles = []
    for k in range(len(data)):
        row = data[k]
        for i in range(len(row)):
            isVisibleFromTheLeft = True
            isVisibleFromTheRight = True
            for j in range(len(row)):
                if j > i and row[i] <= row[j]:
                    isVisibleFromTheLeft = False
                if i > j and row[i] <= row[j]:
                    isVisibleFromTheRight = False
            if isVisibleFromTheLeft or isVisibleFromTheRight:
                indicesArbresVisibles.append(str(k)+"_"+str(i))
    dataTransposed = []
    for i in range(len(data[0])):
        r = ''
        for j in range(len(data)):
            r += data[j][i]
        dataTransposed.append(r)
    # meme chose sur donnee transposee
    for k in range(len(dataTransposed)):
        row = dataTransposed[k]
        for i in range(len(row)):
            isVisibleFromTheTop = True
            isVisibleFromTheBot = True
            for j in range(len(row)):
                if i > j and row[i] <= row[j]:
                    isVisibleFromTheTop = False
                if j > i and row[i] <= row[j]:
                    isVisibleFromTheBot = False
            if isVisibleFromTheTop or isVisibleFromTheBot:
                indicesArbresVisibles.append(str(i)+"_"+str(k))
    return(len(set(indicesArbresVisibles)))


print(part1("day8.txt"))
# 1763


def part2(path):
    file = open(path)
    data = file.read().splitlines()
    rangeArbres = {}
    for k in range(len(data)):
        row = data[k]
        for i in range(len(row)):
            rangeLeft = i
            rangeRight = len(row)-i-1
            for j in range(len(row)):
                if j > i and row[i] <= row[j]:
                    rangeRight = min(rangeRight, j-i)
                if i > j and row[i] <= row[j]:
                    rangeLeft = min(rangeLeft, i-j)
            rangeArbres[str(k)+"_"+str(i)] = rangeLeft*rangeRight
    dataTransposed = []
    for i in range(len(data[0])):
        r = ''
        for j in range(len(data)):
            r += data[j][i]
        dataTransposed.append(r)
    # meme chose sur donnee transposee
    for k in range(len(dataTransposed)):
        row = dataTransposed[k]
        for i in range(len(row)):
            rangeLeft = i
            rangeRight = len(row)-i-1
            for j in range(len(row)):
                if j > i and row[i] <= row[j]:
                    rangeRight = min(rangeRight, j-i)
                if i > j and row[i] <= row[j]:
                    rangeLeft = min(rangeLeft, i-j)
            a = rangeArbres[str(i)+"_"+str(k)]
            rangeArbres[str(i)+"_"+str(k)] = a * rangeLeft*rangeRight

    return(max(rangeArbres.values()))


print(part2("day8.txt"))
# 671160
