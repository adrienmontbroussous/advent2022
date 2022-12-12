

import numpy as np


def jouerTour(i, monkeys):
    itemsApresScore = []
    for item in monkeys[i]["items"]:
        if monkeys[i]["operation"] == "addition":
            itemsApresScore.append(
                (item+monkeys[i]["operant"])//3)
        else:
            if(monkeys[i]["operant"] == "old"):
                itemsApresScore.append(
                    (item*item)//3)

            else:
                m = monkeys[i]
                itemsApresScore.append((item*m["operant"])//3)
        monkeys[i]["number_of_inspection"] = monkeys[i]["number_of_inspection"]+1
    for itemApresScore in itemsApresScore:
        if itemApresScore % monkeys[i]["diviseur"] == 0:
            indiceDestinataire = monkeys[i]["destinataire_true"]
            monkeys[indiceDestinataire]["items"].append(itemApresScore)
        else:
            indiceDestinataire = monkeys[i]["destinataire_false"]
            monkeys[indiceDestinataire]["items"].append(itemApresScore)
    monkeys[i]["items"] = []
    return monkeys


# monkey={"items":[],"operation":"addition","operant":10,"diviseur"=15,"destainataire_true":1,"destinataire_false":2}


def part1(path):
    file = open(path)
    data = file.read().splitlines()
    monkeys = []
    for i in range((len(data)+1)//7):
        numeroMonkey = i
        items = data[i*7+1].split(':')[1].split(',')
        items = list(map(int, items))
        operation = ''
        operant = 0
        if "*" in data[i*7+2]:
            operation = "multiplication"
            tp = data[i*7+2].split("*")
            print(tp)
            if tp[len(tp)-1] == " old":
                operant = "old"
            else:
                operant = int(tp[len(tp)-1])
        else:
            operation = "addition"
            tp = data[i*7+2].split("+")
            operant = int(tp[len(tp)-1])
        diviseur = int(data[i*7+3].split("by")[1])
        destinataire_true = int(data[i*7+4].split("monkey")[1])
        destinataire_false = int(data[i*7+5].split("monkey")[1])
        monkey = {"items": items, "operation": operation, "operant": operant, "diviseur": diviseur,
                  "destinataire_true": destinataire_true, "destinataire_false": destinataire_false, "number_of_inspection": 0}
        monkeys.append(monkey)
    k = len(monkeys)
    for i in range(20):
        for j in range(k):
            monkeys = jouerTour(j, monkeys)
    occupation = []
    for monkey in monkeys:
        occupation.append(monkey["number_of_inspection"])

    return(occupation)


# print(part1("day11.txt"))
6087


def jouerTour2(i, monkeys, grandDiviseur):
    itemsApresScore = []
    for item in monkeys[i]["items"]:
        if monkeys[i]["operation"] == "addition":
            itemsApresScore.append(
                (item+monkeys[i]["operant"]))
        else:
            if(monkeys[i]["operant"] == "old"):
                itemsApresScore.append(
                    (item*item))

            else:
                m = monkeys[i]
                itemsApresScore.append((item*m["operant"]))
        monkeys[i]["number_of_inspection"] = monkeys[i]["number_of_inspection"]+1
    for itemApresScore in itemsApresScore:
        # On peut ne s'intéresser qu'au reste de la division par le produit des diviseurs. (tout nombre multiple de ce produit le sera toujours)
        # le cas 0 est accepté dans cette version de code car on regarde le reste
        # semblant d'explication empirique:
        # on sait par quelque manière que x = a*b +C où a est le diviseur d'un singe
        # a divise donc x ssi a divise C
        # idem pour x = A*b +C
        # avec A=produit des a pour chaque singe
        # on peut donc se débarasser de la partie multiple du produit des diviseurs
        itemModulo = itemApresScore % grandDiviseur
        if itemApresScore % monkeys[i]["diviseur"] == 0:
            indiceDestinataire = monkeys[i]["destinataire_true"]
            monkeys[indiceDestinataire]["items"].append(itemModulo)
        else:
            indiceDestinataire = monkeys[i]["destinataire_false"]
            monkeys[indiceDestinataire]["items"].append(itemModulo)
    monkeys[i]["items"] = []
    return monkeys

# monkey={"items":[],"operation":"addition","operant":10,"diviseur"=15,"destainataire_true":1,"destinataire_false":2}


def part2(path):
    file = open(path)
    data = file.read().splitlines()
    monkeys = []
    for i in range((len(data)+1)//7):
        items = data[i*7+1].split(':')[1].split(',')
        items = list(map(int, items))
        operation = ''
        operant = 0
        if "*" in data[i*7+2]:
            operation = "multiplication"
            tp = data[i*7+2].split("*")
            if tp[len(tp)-1] == " old":
                operant = "old"
            else:
                operant = int(tp[len(tp)-1])
        else:
            operation = "addition"
            tp = data[i*7+2].split("+")
            operant = int(tp[len(tp)-1])
        diviseur = int(data[i*7+3].split("by")[1])
        destinataire_true = int(data[i*7+4].split("monkey")[1])
        destinataire_false = int(data[i*7+5].split("monkey")[1])
        monkey = {"items": items, "operation": operation, "operant": operant, "diviseur": diviseur,
                  "destinataire_true": destinataire_true, "destinataire_false": destinataire_false, "number_of_inspection": 0}
        monkeys.append(monkey)
    k = len(monkeys)
    grandDiviseur = 1
    for monkey in monkeys:
        grandDiviseur = grandDiviseur*monkey["diviseur"]
    for i in range(10000):
        for j in range(k):
            monkeys = jouerTour2(j, monkeys, grandDiviseur)
    occupation = []
    for monkey in monkeys:
        occupation.append(monkey["number_of_inspection"])

    return(occupation)


print(part2("day11.txt"))
# 2493
