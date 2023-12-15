import numpy as np
from hashlib import sha1

with open("day-14.txt", "r") as f:
    input_data = f.read().strip()

m = np.array([list(row) for row in input_data.split("\n")])


def calculate_load(a):
    acc = 0
    for idx, t in np.ndenumerate(a):
        if t == "O":
            acc += len(a) - idx[0]

    return acc


def tilt(a):
    for idx, t in np.ndenumerate(a):
        if t == "O":
            r = idx[0]
            c = idx[1]
            furthest = False
            while furthest == False:
                if a[max(r - 1, 0)][c] != "." or r == 0:
                    furthest = True
                    a[idx[0]][c] = "."
                    a[r][c] = "O"
                else:
                    r -= 1
    return a


# Part 1

m1 = m.copy()
m1 = tilt(m1)

print(calculate_load(m1))

# Part 2


def apply_cycle(a):
    for _ in range(4):
        a = tilt(a)
        a = np.rot90(a, k=1, axes=(1, 0))  # Clockwise rotation

    return a


cycles = 1_000_000_000
viewed = []
i = 0
m2 = m.copy()
while True:
    i += 1
    m2 = apply_cycle(m2)
    hashed = sha1("".join(x for _, x in np.ndenumerate(m2)).encode()).hexdigest()
    if hashed not in viewed:
        viewed.append(hashed)
    else:
        break

p1 = viewed.index(hashed)
period = i - p1 - 1
rep = p1 + (cycles - p1) % period

for _ in range(rep):
    m = apply_cycle(m)

print(calculate_load(m))
