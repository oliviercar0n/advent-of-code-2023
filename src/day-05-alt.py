with open("day-05-puzzle-input.txt", "r") as f:
    input_data = f.read().strip()

parts = input_data.split('\n\n')
seed, *others = parts

seeds = [int(value) for value in seed.split(':')[1].split()]

# Part 1 

def f(s, o):
    for line in o:
        dest, src, size = [int(x) for x in line.split()]
        if src <= s < src+size:
            return s + (dest - src)
    return s

S = []
for s in seeds:
    for o in others:
        O = o.split('\n')
        s = f(s, O[1:])
    S.append(s)

print(min(S))

# Part 2

def f(R, o):
    A = []
    for line in o:
        dest, src, size = [int(x) for x in line.split()]
        src_end = src + size
        NR = []
        while R:
            (st, ed) = R.pop()
            before = (st, min(ed, src))
            inter = (max(st, src), min(src_end, ed))
            after = (max(src_end, st), ed)
            if before[1] > before[0]:
                NR.append(before)
            if inter[1] > inter[0]:
                A.append((inter[0]-src+dest, inter[1]-src+dest))
            if after[1] > after[0]:
                NR.append(after)
        R = NR
    return A+R

S = []
si = 0
while si<len(seeds):
    st, sz = seeds[si], seeds[si+1]
    si += 2
    R = [(st, st+sz)]
    for o in others:
        O = o.split('\n')
        R = f(R, O[1:])
    S.append(min(R)[0])
    
print(min(S))