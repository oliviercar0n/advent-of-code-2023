import numpy as np

with open("day-09.txt", "r") as f:
    input_data = f.read().strip()


lines = input_data.split("\n")
histories = [[int(x) for x in l.split(" ")] for l in lines]

# Part 1

acc = 0
for history in histories:
    ss = history
    seqs = []
    while True:
        ss = np.diff(ss)
        if all(i == 0 for i in ss):
            break
        else:
            seqs.append(ss)

    inc = 0
    for seq in reversed(seqs):
        inc = seq[-1] + inc

    acc += history[-1] + inc

print(acc)

# Part 2

acc = 0
for history in histories:
    ss = history
    seqs = []
    while True:
        ss = np.diff(ss)
        if all(i == 0 for i in ss):
            break
        else:
            seqs.append(ss)

    inc = 0
    for seq in reversed(seqs):
        inc = seq[0] - inc

    acc += history[0] - inc

print(acc)
