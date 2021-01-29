import re
ans = 20151125
row, col = list(map(int, re.findall(r'\d+', open('input.txt').read()))
k = 1 - row
row += col - 1
while row > 0:
    k += row
    row -= 1
while k > 1:
    ans = (ans * 252533) % 33554393
    k -= 1
print(ans)
