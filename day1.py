


def part1(path):
    file=open(path);
    weightCarried=0;
    weightMaxCarried=0
    for row in file:
        if(row=='\n'):
            if weightCarried>weightMaxCarried:
                weightMaxCarried=weightCarried
            weightCarried=0
        else:
            weightCarried=weightCarried+int(row)      
    if weightCarried>weightMaxCarried:
                weightMaxCarried=weightCarried
    return(weightMaxCarried);

print(part1("day1.txt"));

def part2(path):
    file=open(path);
    weightCarried=0;
    weightMaxCarried1=0
    weightMaxCarried2=0
    weightMaxCarried3=0
    for row in file:
        if(row=='\n'):
            if weightCarried>weightMaxCarried1:
                weightMaxCarried3=weightMaxCarried2
                weightMaxCarried2=weightMaxCarried1
                weightMaxCarried1=weightCarried
            else:
                if weightCarried>weightMaxCarried2:
                    weightMaxCarried3=weightMaxCarried2
                    weightMaxCarried2=weightCarried
                else:
                    if weightCarried>weightMaxCarried3:
                        weightMaxCarried3=weightCarried
            weightCarried=0
        else:
            weightCarried=weightCarried+int(row)      
    if weightCarried>weightMaxCarried1:
                weightMaxCarried3=weightMaxCarried2
                weightMaxCarried2=weightMaxCarried1
                weightMaxCarried1=weightCarried
    else:
        if weightCarried>weightMaxCarried2:
            weightMaxCarried3=weightMaxCarried2
            weightMaxCarried2=weightCarried
        else:
            if weightCarried>weightMaxCarried3:
                weightMaxCarried3=weightCarried
    return(weightMaxCarried1+weightMaxCarried2+weightMaxCarried3);


print(part2("day1.txt"));