import json
from  functools import cmp_to_key


    # If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
    # If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
    # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].


def compare_lists(liste1,liste2):
    resultat=0
    for i in range(len(liste1)):
        if i > len(liste2)-1:
            return 1
        elementList1=liste1[i]
        elementList2=liste2[i]
        if isinstance(elementList1, int) and isinstance(elementList2,int):
            if elementList1>elementList2:
                return 1
            if elementList1<elementList2:
                return -1
        if isinstance(elementList1, list) and isinstance(elementList2,list):
            if compare_lists(elementList1,elementList2)!=0:
                return compare_lists(elementList1,elementList2)
        if isinstance(elementList1, list) and isinstance(elementList2, int):
            if compare_lists(elementList1,[elementList2])!=0:
                return compare_lists(elementList1,[elementList2])
        if isinstance(elementList1, int) and isinstance(elementList2, list):
            if compare_lists([elementList1],elementList2)!=0:
                return compare_lists([elementList1],elementList2)
    if resultat==0:
        if len(liste1) < len(liste2):
            return -1
        elif len(liste1) > len(liste2):
            return 1
        else:
            return 0
    return resultat

def part1(path):
    file = open(path)
    data = file.read().splitlines()
    packets=[]
    resultat=0
    for i in range((len(data)+1)//3):
        row1=data[i*3]
        packets.append(json.loads(row1))
        row2=data[i*3+1]
        packets.append(json.loads(row2))
    for i in range(len(packets)//2):
        if compare_lists(packets[2*i],packets[2*i+1]) ==-1:
            resultat=resultat+i+1
    return (resultat)

print(part1("day13.txt"))
#5196 

def part2(path):
    file = open(path)
    data = file.read().splitlines()
    packets=[]
    for i in range((len(data)+1)//3):
        row1=data[i*3]
        packets.append(json.loads(row1))
        row2=data[i*3+1]
        packets.append(json.loads(row2))
    divider1=[[2]]
    packets.append(divider1)
    divider2=[[6]]
    packets.append(divider2)
    packetsSorted=sorted(packets,key=cmp_to_key(compare_lists))
    posDivider1=0
    posDivider2=0
    i=0
    while posDivider1==0 or posDivider2==0:
        if packetsSorted[i]==divider1:
            posDivider1=i+1
        if packetsSorted[i]==divider2:
            posDivider2=i+1
        i=i+1
    return (posDivider1*posDivider2)

print(part2("day13.txt"))

#22134