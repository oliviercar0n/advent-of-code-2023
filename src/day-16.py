import numpy as np

with open("day-16.txt", "r") as f:
    input_data = f.read().strip()

m = np.array([list(row) for row in input_data.split("\n")])


def count_energized(initial_beam, a):
    energized = []
    beam_states = [initial_beam]
    B = [initial_beam]
    while len(B) > 0:
        NB = []
        for pos, d in B:
            if 0 <= pos[0] < m.shape[0] and 0 <= pos[1] < m.shape[1]:
                if pos not in energized:
                    energized.append(pos)
                t = a[pos[0]][pos[1]]
                if t == "\\":
                    d = (d[1], d[0])
                elif t == "/":
                    d = (-d[1], -d[0])
                elif (t == "|" and d[0] == 0) or (t == "-" and d[1] == 0):
                    d = (d[1], d[0])
                    nd = (-d[0], -d[1])
                    npos = tuple(np.add(pos, nd))
                    NB.append((npos, nd))
                pos = tuple(np.add(pos, d))
                if (pos, d) not in beam_states:
                    beam_states.append((pos, d))
                    NB.append((pos, d))
        B = NB

    return len(energized)

# Part 1

initial = ((0, 0), (0, 1))
print(count_energized(initial, m))

# Part 2

total = []
configs = []

# Top
d = (1, 0)
for i in range(m.shape[1]):
    configs.append(((0, i), d))

# Bottom
d = (-1, 0)
for i in range(m.shape[1]):
    configs.append(((m.shape[1] - 1, i), d))

# Left
d = (0, 1)
for i in range(m.shape[0]):
    configs.append(((i, 0), d))

# Right
d = (0, -1)
for i in range(m.shape[0]):
    configs.append(((i, m.shape[0] - 1), d))

for i, config in enumerate(configs):
    total.append(count_energized(config, m))

print(max(total))
