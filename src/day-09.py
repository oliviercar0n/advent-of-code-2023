import numpy as np

with open("day-09-puzzle-input.txt", "r") as f:
    input_data = f.read().strip()


lines = input_data.split("\n")
histories = [[int(x) for x in l.split(" ")] for l in lines]

# Part 1

acc = 0
for history in histories:
    cs = []
    ss = history
    seqs = []
    while True:
        cs = np.diff(ss)
        if all(i == 0 for i in cs):
            break
        else:
            seqs.append(cs)
        ss = cs
    
    inc = 0
    for seq in reversed(seqs):
        inc = seq[-1] + inc
    
    acc += history[-1] + inc

print(acc)

# Part 2

acc = 0
for history in histories:
    cs = []
    ss = history
    seqs = []
    while True:
        cs = np.diff(ss)
        if all(i == 0 for i in cs):
            break
        else:
            seqs.append(cs)
        ss = cs

    inc = 0
    for seq in reversed(seqs):
        inc = seq[0] - inc
    
    acc += history[0] - inc
    
print(acc)