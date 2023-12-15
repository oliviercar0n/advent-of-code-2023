import numpy as np
from collections import defaultdict

with open("day-15.txt", "r") as f:
    input_data = f.read().strip()


def hash_fn(step):
    v = 0
    for c in step:
        if c != "\n":
            v += ord(c)
            v = v * 17
            v = v % 256

    return v


acc = 0
for step in input_data.split(","):
    acc += hash_fn(step)

print(acc)

# Part 2

B = defaultdict(dict)
i = 0
for step in input_data.split(","):
    if "=" in step:
        label, fl = step.split("=")
        box = hash_fn(label)
        B[box][label] = int(fl)
    elif "-" in step:
        label = step.split("-")[0]
        box = hash_fn(label)
        if label in B[box].keys():
            del B[box][label]

acc = 0
for box_num, lenses in B.items():
    for idx, label in enumerate(lenses.keys()):
        acc += (1 + box_num) * (idx + 1) * B[box_num][label]

print(acc)
