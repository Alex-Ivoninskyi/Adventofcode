import numpy as np
import re
array = np.reshape(list(map(int, re.findall(r'\d+', open('input.txt').read()))),  (-1, 3))
ans = 0
for curr in array:
    l, w, h = sorted(curr)
    ans += 3 * l * w + 2 * (l * h + w * h)
print(ans)
