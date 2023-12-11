import numpy as np
from itertools import combinations

with open("day-11.txt", "r") as f:
    input_data = f.read().strip()

a = np.array([list(row) for row in input_data.split("\n")])

# Part 1

m = a
er = []
for i, row in enumerate(m):
    if "#" not in row:
        er.append(i)

for i, r in enumerate(er):
    m = np.insert(m, r + i + 1, ".", axis=0)

ec = []
for i, col in enumerate(m.T):
    if "#" not in col:
        ec.append(i)
for i, c in enumerate(ec):
    m = np.insert(m, c + i + 1, ".", axis=1)

G = list(zip(*np.where(m == "#")))
pairs = list(combinations(G, 2))

D = []
for g1, g2 in pairs:
    dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    D.append(dist)

print(sum(D))

# Part 2

G = list(zip(*np.where(a == "#")))

inc = 1_000_000 - 1
cnt = 0
for i, row in enumerate(a):
    if "#" not in row:
        NG = []
        for g in G:
            if g[0] > i + (cnt * inc):
                ng = (g[0] + inc, g[1])
            else:
                ng = g
            NG.append(ng)
        G = NG
        cnt += 1

cnt = 0
for i, col in enumerate(a.T):
    if "#" not in col:
        NG = []
        for g in G:
            if g[1] > i + (cnt * inc):
                ng = (g[0], g[1] + inc)
            else:
                ng = g
            NG.append(ng)
        G = NG
        cnt += 1

pairs = list(combinations(G, 2))

D = []
for g1, g2 in pairs:
    dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    D.append(dist)

print(sum(D))
