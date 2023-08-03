x, y, w, h = map(int, input().split())
import math
if x<w and y<h:
    print(min(x, y, w-x, h-y))
elif x>w and y<h:
    print(x-w)
elif x<w and y>h:
    print(h-y)
else:
    print(math.sqrt((x-w)**2+(y-h)**2))