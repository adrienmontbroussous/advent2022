


def part1(path):
    file=open(path);
    pointsPlayer=0;

    for row in file:
        if row[0]=="A" and row[2]=="X":
            pointsPlayer=pointsPlayer+4
        if row[0]=="A" and row[2]=="Y":
            pointsPlayer=pointsPlayer+8
        if row[0]=="A" and row[2]=="Z":
            pointsPlayer=pointsPlayer+3
        if row[0]=="B" and row[2]=="X":
            pointsPlayer=pointsPlayer+1
        if row[0]=="B" and row[2]=="Y":
            pointsPlayer=pointsPlayer+5
        if row[0]=="B" and row[2]=="Z":
            pointsPlayer=pointsPlayer+9
        if row[0]=="C" and row[2]=="X":
            pointsPlayer=pointsPlayer+7
        if row[0]=="C" and row[2]=="Y":
            pointsPlayer=pointsPlayer+2
        if row[0]=="C" and row[2]=="Z":
            pointsPlayer=pointsPlayer+6

    return(pointsPlayer);

print(part1("day2.txt"));


def part2(path):
    file=open(path);
    pointsPlayer=0;

    for row in file:
        if row[0]=="A" and row[2]=="X":#play Scissors  to lose
            pointsPlayer=pointsPlayer+3
        if row[0]=="A" and row[2]=="Y":#play rock to draw
            pointsPlayer=pointsPlayer+4
        if row[0]=="A" and row[2]=="Z":#play paper to win
            pointsPlayer=pointsPlayer+8
        if row[0]=="B" and row[2]=="X":#play rock to lose
            pointsPlayer=pointsPlayer+1
        if row[0]=="B" and row[2]=="Y":#play paper to draw
            pointsPlayer=pointsPlayer+5
        if row[0]=="B" and row[2]=="Z":#play Scissors  win
            pointsPlayer=pointsPlayer+9
        if row[0]=="C" and row[2]=="X":#play paper to lose
            pointsPlayer=pointsPlayer+2
        if row[0]=="C" and row[2]=="Y":#play Scissors  to draw
            pointsPlayer=pointsPlayer+6
        if row[0]=="C" and row[2]=="Z":#play rock to win
            pointsPlayer=pointsPlayer+7

    return(pointsPlayer);

print(part2("day2.txt"));