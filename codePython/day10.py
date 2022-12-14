

import numpy as np


def part1(path):
    file = open(path)
    data = file.read().splitlines()
    x = 1
    instructions = []
    cyclesExecuted = 1
    signalStrength = []

    for row in data:
        value = ""
        commande = row.split(" ")[0]
        if len(row.split(" ")) == 2:
            value = int(row.split(" ")[1])
        instructions.append([commande, value])
    for instruction in instructions:
        commande, value = instruction[0], instruction[1]
        if cyclesExecuted == 19+len(signalStrength)*40 or cyclesExecuted == 20+len(signalStrength)*40:
            print(x)
            print(cyclesExecuted)
            signalStrength.append(x*(20+len(signalStrength)*40))
        if commande == "noop":
            cyclesExecuted = cyclesExecuted+1
        if commande == "addx":
            cyclesExecuted = cyclesExecuted+2
            x = x+value

    return(sum(signalStrength))


# print(part1("day10.txt"))
# 6087


def part2(path):
    file = open(path)
    data = file.read().splitlines()
    x = 1
    instructions = []
    cyclesExecuted = 1
    screen = [["." for i in range(40)] for i in range(6)]

    for row in data:
        value = ""
        commande = row.split(" ")[0]
        if len(row.split(" ")) == 2:
            value = int(row.split(" ")[1])
        instructions.append([commande, value])
    for instruction in instructions:
        commande, value = instruction[0], instruction[1]
        row = cyclesExecuted//40
        positionCurseur = (cyclesExecuted) % 40 - 1
        if commande == "noop":
            if positionCurseur in (x-1, x, x+1):
                screen[row][positionCurseur] = "#"
            cyclesExecuted = cyclesExecuted+1
        if commande == "addx":
            for i in range(2):
                if positionCurseur in (x-1, x, x+1):
                    print(row)
                    screen[row][positionCurseur] = "#"
                cyclesExecuted = cyclesExecuted+1
                positionCurseur = positionCurseur+1
            x = x+value
    with open('result.txt', 'w') as f:
        for line in screen:
            f.write(''.join(line))
            f.write('\n')


part2("day10.txt")


# print(part2("day9.txt"))
# 2493
