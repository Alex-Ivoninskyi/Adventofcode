way = open('input.txt').read()
si = 0
sj = 0
ri = 0
rj = 0
x = 0
ans = 1
hist = [[0, 0]]
for step in way:
    x += 1
    if x % 2 == 1:
        if step == '>':
            sj += 1
        if step == '^':
            si += 1
        if step == '<':
            sj -= 1
        if step == 'v':        
            si -= 1
        check = 0 
        for coor in hist:
            if [si, sj] == coor:
                check += 1
        if check == 0:
            hist += [[si, sj]]
            ans += 1
    else:
        if step == '>':
            rj += 1
        if step == '^':
            ri += 1
        if step == '<':
            rj -= 1
        if step == 'v':        
            ri -= 1
        check = 0 
        for coor in hist:
            if [ri, rj] == coor:
                check += 1
        if check == 0:
            hist += [[ri, rj]]
            ans += 1
print(ans)
