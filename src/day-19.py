import numpy as np
import re

with open("day-19.txt", "r") as f:
    input_data = f.read().strip()


# Part 1

workflows, parts = input_data.split("\n\n")

W = {}
def process_workflow(w, ratings):
    for s in W[w]:
        if len(s) == 1:
            return s
        elif ":" in s:
            rule, dest = s.split(":")
            if ">" in rule:
                r, v = rule.split(">")
                v = int(v)
                if int(ratings[r]) > v:
                    if len(dest) == 1:
                        return dest
                    else:
                        return process_workflow(dest, ratings)
            elif "<" in rule:
                r, v = rule.split("<")
                v = int(v)
                if int(ratings[r]) < v:
                    if len(dest) == 1:
                        return dest
                    else:
                        return process_workflow(dest, ratings)
        else:
            return process_workflow(s, ratings)


for w in workflows.split("\n"):
    name, steps = w.split("{")
    steps = steps[:-1]
    W[name] = steps.split(",")

acc = 0
for p in parts.split("\n"):
    p = p[1:-1]
    ratings = dict(zip(["x", "m", "a", "s"], re.findall("\d+", p)))
    result = process_workflow("in", ratings)
    if result == 'A':
        acc += sum(int(x) for x in ratings.values()) 


print(acc)

# Part 2