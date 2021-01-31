ans = 0
for temp in (open('input.txt').read()).split('\n'):
    l, w, h = sorted([int(x) for x in temp.split('x')])
    ans += 3 * l * w + 2 * (l * h + w * h)
print(ans)
