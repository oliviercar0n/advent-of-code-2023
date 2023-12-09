from collections import defaultdict
from math import lcm

with open("day-08-puzzle-input.txt", "r") as f:
    input_data = f.read().strip()

data = input_data.split("\n")

directions = data[0]

m = defaultdict()
nodes = data[2:]

for node in nodes:
    n, steps = node.split('=')
    p = steps.split(',')
    s = (p[0].strip()[1:],p[1].strip()[:-1])
    m[n.strip()] = s

# Part 1

i = 0
n =0
c_node = 'AAA'
while c_node != 'ZZZ':
    for d in directions:
        i+=1
        if d == 'L':
            c_node = m[c_node][0]
        elif d == 'R':
            c_node = m[c_node][1] 

        if c_node == 'ZZZ':
            break       

print(i)

# Part 2

s = [node for node in m.keys() if node.endswith('A')]

mm = []
for c_node in s:
    i = 0
    while not c_node.endswith('Z'):
        for d in directions:
            i+=1
            if d == 'L':
                c_node = m[c_node][0]
            elif d == 'R':
                c_node = m[c_node][1] 

            if c_node.endswith('Z'):
                mm.append(i)
                break

print(lcm(*mm))