import numpy as np


with open("day-10.txt", "r") as f:
    input_data = f.read().strip()

m = np.array([list(row) for row in input_data.split("\n")])

pd = {
    "|": {(-1, 0): (-1, 0), (1, 0): (1, 0)},
    "-": {(0, 1): (0, 1), (0, -1): (0, -1)},
    "L": {(1, 0): (0, 1), (0, -1): (-1, 0)},
    "J": {(1, 0): (0, -1), (0, 1): (-1, 0)},
    "7": {(-1, 0): (0, -1), (0, 1): (1, 0)},
    "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
}

allowed = {
    (-1, 0): ["|", "7", "F"],  # UP
    (1, 0): ["|", "L", "J"],  # DOWN
    (0, 1): ["-", "7", "J"],  # RIGHT
    (0, -1): ["-", "F", "L"],  # LEFT
}

# Part 1

sc = list(zip(*np.where(m == "S")))[0]


# Find first pipe
for d in [(-1, 0), (1, 0), (0, 1), (0, 1)]:
    cp = np.add(sc, d)
    pipe = m[cp[0], cp[1]]
    if pipe in allowed[d]:
        sd = d
        break

cd = sd
i = 0
cp = sc
while True:
    i += 1
    cp = np.add(cd, cp)
    pipe = m[cp[0], cp[1]]
    if pipe == "S":
        break
    cd = pd[pipe][cd]

print(int(i / 2))

# Part 2

cd = sd
i = 0
nm = m
cp = sc

while True:
    i += 1
    cp = np.add(cd, cp)
    pipe = m[cp[0], cp[1]]
    nm[cp[0], cp[1]] = "X"

    if pipe in ["F", "7", "|"]:
        nm[cp[0], cp[1]] = "x"
    if pipe == "S":
        break

    cd = pd[pipe][cd]

acc = 0
for j in range(0, nm.shape[0] - 1):
    for i in range(0, nm.shape[1] - 1):
        it = 0
        if nm[j][i] not in ["X", "x"]:
            for x in range(i, nm.shape[1]):
                if nm[j][x] == "x":
                    it += 1
        if it % 2 > 0:
            acc += 1

print(acc)
