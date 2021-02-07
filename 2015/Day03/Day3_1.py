way = open('input.txt').read()
i = 0
j = 0
ans = 1
hist = [[0, 0]]
for step in way:
    if step == '>':
        j += 1
    if step == '^':
        i += 1
    if step == '<':
        j -= 1
    if step == 'v':        
        i -= 1
    check = 0 
    for coor in hist:
        if [i, j] == coor:
            check += 1
    if check == 0:
        hist += [[i, j]]
        ans += 1
print(ans)
        
