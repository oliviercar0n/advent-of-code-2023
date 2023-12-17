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

# Part 1

print(sum(hash_fn(step) for step in input_data.split(",")))

# Part 2

B = defaultdict(dict)
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
    for idx, (label, fl) in enumerate(lenses.items()):
        acc += (1 + box_num) * (idx + 1) * fl

print(acc)
