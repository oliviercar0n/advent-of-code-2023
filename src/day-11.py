import numpy as np
from itertools import combinations

with open("day-11-puzzle-input.txt", "r") as f:
    input_data = f.read().strip()

a = np.array([list(row) for row in input_data.split("\n")])

# Part 1

m = a
er = []
for i, row in enumerate(m):
    if "#" not in np.unique(row):
        er.append(i)

for i, r in enumerate(er):
    m = np.insert(m, r + i + 1, ".", axis=0)

ec = []
for i, col in enumerate(m.T):
    if "#" not in np.unique(col):
        ec.append(i)
for i, r in enumerate(ec):
    m = np.insert(m, r + i + 1, ".", axis=1)

G = list(zip(*np.where(m == "#")))
pairs = list(combinations(G, 2))

D = []
for pair in pairs:
    dist = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
    D.append(dist)

print(sum(D))

# Part 2

G = list(zip(*np.where(a == "#")))

inc = 1_000_000 - 1
cnt = 0
for i, row in enumerate(a):
    if "#" not in np.unique(row):
        NG = []
        for g in G:
            if g[0] > i+(cnt*inc):
                ng = (g[0]+inc, g[1])
            else:
                ng = g 
            NG.append(ng)
        G = NG
        cnt += 1
        
cnt = 0
for i, col in enumerate(a.T):
    if "#" not in np.unique(col):
        NG = []
        for g in G:
            if g[1] > i+(cnt*inc):
                ng = (g[0],g[1]+inc)
            else:
                ng = g 
            NG.append(ng)
        G = NG
        cnt += 1

pairs = list(combinations(G, 2))

D = []
for pair in pairs:
    dist = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
    D.append(dist)

print(sum(D))