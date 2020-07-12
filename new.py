import numpy as np
from math import sqrt

base_length = '144 189 230 219 215' 
hight = '94 105 146.6 105 144'

# base_length = str(input())
# hight = str(input())

base_length = np.array(base_length.split(), dtype=float)
hight = np.array(hight.split(), dtype=float)

p = [x for x in base_length *4]
s = [x for x in base_length ** 2]
r = [x for x in base_length / 2]
v = []
d = []
side_s = []
for s, h in zip(s, hight):
    v.append(1/3 * s * h)

for h, r in zip(hight, r):
    d.append(sqrt(h ** 2 + r ** 2))

for d, p in zip(d, p):
    side_s.append(1/2 * d * p)


print("Vmax: %2d, %8.2f, Smin: %2d, %8.2f" % (np.where(v == max(v))[0][0], max(v), np.where(side_s == min(side_s))[0][0], min(side_s)))
