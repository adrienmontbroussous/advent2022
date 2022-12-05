

def part1(path):
    file = open(path)
    rows = file.read().splitlines()

    indexesStacks = []

    for i in range(len(rows[8])):
        if(rows[8][i:i+1] != ' '):
            indexesStacks.append(i)
    numberOfStacks = len(indexesStacks)
    stacks = [[] for i in range(numberOfStacks)]
    for i in range(numberOfStacks):
        index = indexesStacks[i]
        for j in range(8):
            if rows[7-j][index] != " ":
                stacks[i].append(rows[7-j][index])
    for i in range(10, len(rows)):
        splited = rows[i].split(" ")
        amount = int(splited[1])
        depart = int(splited[3])-1
        destination = int(splited[5])-1
        for j in range(amount):
            moving = stacks[depart].pop()
            stacks[destination].append(moving)
    #instructions : line
    result = ""
    for i in range(len(stacks)):
        result = result+stacks[i][len(stacks[i])-1]
    return(result)


print(part1("day5.txt"))


def part2(path):
    file = open(path)
    rows = file.read().splitlines()

    indexesStacks = []

    for i in range(len(rows[8])):
        if(rows[8][i:i+1] != ' '):
            indexesStacks.append(i)
    numberOfStacks = len(indexesStacks)
    stacks = [[] for i in range(numberOfStacks)]
    for i in range(numberOfStacks):
        index = indexesStacks[i]
        for j in range(8):
            if rows[7-j][index] != " ":
                stacks[i].append(rows[7-j][index])
    for i in range(10, len(rows)):
        splited = rows[i].split(" ")
        amount = int(splited[1])
        depart = int(splited[3])-1
        destination = int(splited[5])-1
        # in order to preserve the order of containers moved
        # we move them to a temporary stack and after to the real destination
        temporaryStack = []
        for j in range(amount):
            moving = stacks[depart].pop()
            temporaryStack.append(moving)
        for k in range(amount):
            moving2 = temporaryStack.pop()
            stacks[destination].append(moving2)
    #instructions : line
    result = ""
    for i in range(len(stacks)):
        result = result+stacks[i][len(stacks[i])-1]
    return(result)


print(part2("day5.txt"))
