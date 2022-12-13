
def moveHead(x, y, instruction):
    if instruction == 'R':
        x = x+1
    elif instruction == 'L':
        x = x-1
    elif instruction == 'D':
        y = y-1
    else:
        y = y+1
    return x, y


def moveTail(xH, yH, xT, yT):
    if (abs(xH-xT) == 2 and abs(yH-yT) == 0):
        xT = int(xT+(xH-xT)/2)
    elif(abs(xH-xT) == 0 and abs(yH-yT) == 2):
        yT = int(yT+(yH-yT)/2)
    else:
        if not (abs(xH-xT) in (0, 1) and abs(yH-yT) in (0, 1)):
            xT = int(xT+(xH-xT)/abs(xH-xT))
            yT = int(yT+(yH-yT)/abs(yH-yT))
    return xT, yT


def part1(path):
    file = open(path)
    data = file.read().splitlines()
    xH = 0
    yH = 0
    xT = 0
    yT = 0
    visitedByT = []
    for row in data:
        instruction, numberOfRepetition = row.split(" ")
        numberOfRepetition = int(numberOfRepetition)
        for i in range(numberOfRepetition):
            xH, yH = moveHead(xH, yH, instruction)
            xT, yT = moveTail(xH, yH, xT, yT)
            visitedByT.append(str(xT)+"_"+str(yT))
    return(len(set(visitedByT)))


print(part1("day9.txt"))
# 6087


def part2(path):
    file = open(path)
    data = file.read().splitlines()
    x = [0 for i in range(10)]
    y = [0 for i in range(10)]
    visitedByT = []
    for row in data:
        instruction, numberOfRepetition = row.split(" ")
        numberOfRepetition = int(numberOfRepetition)
        for i in range(numberOfRepetition):
            for j in range(10):
                if j == 0:
                    x[j], y[j] = moveHead(x[j], y[j], instruction)
                else:
                    x[j], y[j] = moveTail(x[j-1], y[j-1], x[j], y[j])
            visitedByT.append(str(x[9])+"_"+str(y[9]))
    return(len(set(visitedByT)))


print(part2("day9.txt"))
# 2493
