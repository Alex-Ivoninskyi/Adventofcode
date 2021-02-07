import re


lines = open('input.txt').read().split('\n')
result = 0
time = 2503
result_name = ''
for line in lines:
    line = line.split()
    speed = int(line[3])
    ttime = int(line[6])
    rest = int(line[13])
    temp = time % (ttime + rest)
    if ttime <= temp:
        count = ttime
    else:
        count = temp
    dist = ((time // (ttime + rest)) * ttime + count) * speed
    if dist > result:
        result = dist
print(result)
