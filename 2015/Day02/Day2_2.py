import numpy as np
import re
array = np.reshape(list(map(int, re.findall(r'\d+', open('input.txt').read()))),  (-1, 3))
ans = 0
for curr in array:
    l, w, h = sorted(curr)
    ans += l * w * h + 2 * (l + w)
print(ans)
