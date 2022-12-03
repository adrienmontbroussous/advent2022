
def part1(path):
    file=open(path);
    total=0;
    for row in file:
        typePresentInBoth=[]
        length=len(row)-1
        firstPart=row[:int(length/2)]
        secondPart=row[int(length/2):]
        for i in range(int(length/2)):
            priority=0;
            char=firstPart[i]
            if char in secondPart:
                if char not in typePresentInBoth:
                    typePresentInBoth.append(char)
        for char2 in typePresentInBoth:
            priority=ord(char2) - 96 + 58 * char2.isupper()
            total=total+priority;
    return(total);

print(part1("day3.txt"));


def part2(path):
    file=open(path);
    rows=file.read().strip().splitlines()
    total=0;
    badges=[]
    for i in range(len(rows)//3):
        badge=''
        for char in rows[i*3]:
            if char in rows[i*3+1] and char in rows[i*3+2]:
                badge=char
        if len(badge)>0:
            badges.append(badge)
    for char2 in badges:
        priority=ord(char2) - 96 + 58 * char2.isupper()
        total=total+priority;
    return(total);

print(part2("day3.txt"))

