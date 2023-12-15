import numpy as np
from itertools import combinations, product
from collections import Counter, defaultdict
from functools import cache


with open("day-12.txt", "r") as f:
    input_data = f.read().strip()


@cache
def compute_arrangement(springs):
    nsp = list(springs)
    G = []
    gs = []
    for j, s in enumerate(springs):
        if s == "#":
            gs.append(s)
        if (s == "." and j > 0) or (j == len(springs) - 1):
            if len(gs) > 0:
                G.append(gs)
                gs = []

    config = [len(x) for x in G]
    return config


@cache
def count_possibilities(springs, arr):
    arr = [int(x) for x in arr.split(",")]
    acc = 0
    c = Counter(sp)["?"]
    for p in list(product(".#", repeat=c)):
        i = 0
        nsp = list(springs)
        for j, s in enumerate(nsp):
            if s == "?":
                nsp[j] = p[i]
                i += 1
        config = compute_arrangement("".join(nsp))
        if config == arr:
            acc += 1

    return acc


# Part 1 (Super naive)

acc = 0
for xx, line in enumerate(input_data.split("\n")[:]):
    print(xx)
    sp, arr = line.split(" ")
    sp = sp.strip()
    acc += count_possibilities(sp, arr)

print(acc)
