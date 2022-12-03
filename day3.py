


def part1(path):
    file=open(path);
    total=0;

    for row in file:
        length=len(row)
        firstPart=row[0:len(row)/2-1]
        secondPart=row[len(row)/2:len(row)-1]
        for i in range(len(row)/2):
            priority=0;
            char=firstPart[i]
            if secondPart.find(char):
                if ord(char)-96>0:
                    priority=ord(char)-96
                else:
                    priority=ord(char)-38
                total=total+priority=;
    return(total);

print(part1("day3.txt"));

