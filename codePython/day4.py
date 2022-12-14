

def part1(path):
    file = open(path)
    rows = file.read().strip().splitlines()
    total = 0
    for i in range(len(rows)):
        elfs = rows[i].split(',')
        firstArea = elfs[0].split('-')
        secondArea = elfs[1].split('-')
        minFirstArea = int(firstArea[0])
        minsecondArea = int(secondArea[0])
        maxFirstArea = int(firstArea[1])
        maxsecondArea = int(secondArea[1])
        if (minFirstArea <= minsecondArea and maxFirstArea >= maxsecondArea) or (minFirstArea >= minsecondArea and maxsecondArea >= maxFirstArea):
            total = total+1
    return(total)


print(part1("day4.txt"))


def part2(path):
    file = open(path)
    rows = file.read().strip().splitlines()
    total = 0
    for i in range(len(rows)):
        elfs = rows[i].split(',')
        firstArea = elfs[0].split('-')
        secondArea = elfs[1].split('-')
        minFirstArea = int(firstArea[0])
        minsecondArea = int(secondArea[0])
        maxFirstArea = int(firstArea[1])
        maxsecondArea = int(secondArea[1])
        if (minsecondArea <= maxFirstArea and maxsecondArea >= minFirstArea) or (minFirstArea <= maxsecondArea and maxFirstArea >= minsecondArea):
            total = total+1
    return(total)


print(part2("day4.txt"))
