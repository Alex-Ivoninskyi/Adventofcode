import re


lines = open('input.txt').read().split('\n')
result = 0
List = []
for line in lines:
    line = line.split()
    speed = int(line[3])#0
    ttime = int(line[6])#1
    rest = int(line[13])#2
    score = 0           #3
    dist = 0            #4
    List.append([speed, ttime, rest, score, dist])
for time in range(1,2504):
    for num in range(0, len(List)):
        temp = time % (List[num][1] + List[num][2])
        count = temp
        if List[num][1] <= temp:
            count = List[num][1]
        List[num][4] = ((time // (List[num][1] + List[num][2]) * List[num][1] + count) * List[num][0])
        if List[num][4] > result:
            result = List[num][4]
    for num in range(0, len(List)):
        if List[num][4] == result:
            List[num][3] += 1    
    result = 0
print(max(List, key = lambda List : List[3])[3])

