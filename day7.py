

import sys

# Attention ca pique les yeux, du franglais et puis il aurait fallu utiliser des arbres surement
# à essayer de refaire proprement


def part1(path):
    file = open(path)
    data = file.read().splitlines()
    content = {"/": {"level": 1,
                     "parent": "", "racineFilesSize": 0}}
    currentDirectory = ""
    level = 0
    for i in range(len(data)):
        row = data[i]
        if row[0] == "$":
            if row[2:4] == "cd":
                if row[5:7] == "..":
                    level = level-1
                    currentDirectory = content[currentDirectory]["parent"]
                else:
                    level = level+1
                    currentDirectory = currentDirectory + row[5:len(row)]
        else:
            size, na = row.split(" ")
            name = currentDirectory+na
            if size == "dir":
                content[name] = {"level": level+1,
                                 "parent": currentDirectory, "racineFilesSize": 0}
            else:
                taille = int(size)
                content[currentDirectory]["racineFilesSize"] = content[currentDirectory]["racineFilesSize"] + taille
    tailleTotaleDesDossier = {}
    maxLevel = 0

    for key, value in content.items():
        maxLevel = max(maxLevel, value['level'])
    for i in range(maxLevel):
        # on traite d'abord les élement de plus bas niveau
        for name, value in content.items():
            if int(value['level']) == maxLevel-i:
                listeDossierEnfants = []
                resultat = 0
                for nom, directory in content.items():
                    if directory["parent"] == name:
                        listeDossierEnfants.append(nom)
                if len(listeDossierEnfants) == 0:
                    tailleTotaleDesDossier[name] = content[name]["racineFilesSize"]
                else:
                    resultat = content[name]["racineFilesSize"]
                    for dossierEnfant in listeDossierEnfants:
                        tailleDossierEnfant = tailleTotaleDesDossier[dossierEnfant]
                        resultat = resultat + tailleDossierEnfant
                    tailleTotaleDesDossier[name] = resultat
    sommeTaillePetitsDossiers = 0
    for key, value in tailleTotaleDesDossier.items():
        if value <= 100000:
            sommeTaillePetitsDossiers = sommeTaillePetitsDossiers+value
    return(sommeTaillePetitsDossiers)


print(part1("day7.txt"))
# 1844187


def part2(path):
    file = open(path)
    data = file.read().splitlines()
    content = {"/": {"level": 1,
                     "parent": "", "racineFilesSize": 0}}
    currentDirectory = ""
    level = 0
    for i in range(len(data)):
        row = data[i]
        if row[0] == "$":
            if row[2:4] == "cd":
                if row[5:7] == "..":
                    level = level-1
                    currentDirectory = content[currentDirectory]["parent"]
                else:
                    level = level+1
                    currentDirectory = currentDirectory + row[5:len(row)]
        else:
            size, na = row.split(" ")
            name = currentDirectory+na
            if size == "dir":
                content[name] = {"level": level+1,
                                 "parent": currentDirectory, "racineFilesSize": 0}
            else:
                taille = int(size)
                content[currentDirectory]["racineFilesSize"] = content[currentDirectory]["racineFilesSize"] + taille
    tailleTotaleDesDossier = {}
    maxLevel = 0

    for key, value in content.items():
        maxLevel = max(maxLevel, value['level'])
    for i in range(maxLevel):
        # on traite d'abord les élement de plus bas niveau
        for name, value in content.items():
            if int(value['level']) == maxLevel-i:
                listeDossierEnfants = []
                resultat = 0
                for nom, directory in content.items():
                    if directory["parent"] == name:
                        listeDossierEnfants.append(nom)
                if len(listeDossierEnfants) == 0:
                    tailleTotaleDesDossier[name] = content[name]["racineFilesSize"]
                else:
                    resultat = content[name]["racineFilesSize"]
                    for dossierEnfant in listeDossierEnfants:
                        tailleDossierEnfant = tailleTotaleDesDossier[dossierEnfant]
                        resultat = resultat + tailleDossierEnfant
                    tailleTotaleDesDossier[name] = resultat
    espaceRestant = 70000000-tailleTotaleDesDossier["/"]
    tailleMinNecessaire = 30000000-espaceRestant
    tailleDirectoryRemplissantCondition = tailleTotaleDesDossier["/"]
    for value in tailleTotaleDesDossier.values():
        if value > tailleMinNecessaire:
            tailleDirectoryRemplissantCondition = min(
                tailleDirectoryRemplissantCondition, value)
    return(tailleDirectoryRemplissantCondition)


print(part2("day7.txt"))
# 4978279
