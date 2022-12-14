

def part1(path):
    file = open(path)
    data = file.readlines()[0]
    i = 0
    result = 4
    keepSearching = True
    while keepSearching:
        toTestForMarker = [data[i], data[i+1], data[i+2], data[i+3]]
        if len(toTestForMarker) == len(set(toTestForMarker)):
            result = i+4
            keepSearching = False
        else:
            i = i+1

    return(result)


print(part1("day6.txt"))


def part2(path):
    file = open(path)
    data = file.readlines()[0]
    i = 0
    result = 14
    keepSearching = True
    while keepSearching:
        toTestForMarker = [data[i+j] for j in range(14)]
        if len(toTestForMarker) == len(set(toTestForMarker)):
            result = i+14
            keepSearching = False
        else:
            i = i+1

    return(result)


print(part2("day6.txt"))
