import numpy as np


with open("day-13.txt", "r") as f:
    input_data = f.read().strip()

patterns = input_data.split("\n\n")


def process_grid(m, axis=0):
    lines = [0]
    if axis == 1:
        nm = m.T
    else:
        nm = m
    for i, row in enumerate(nm[:-1]):
        if np.array_equal(row, nm[i + 1]):
            ok = True
            in1 = i
            in2 = i + 1
            while in1 >= 0 and in2 <= len(nm) - 1:
                if not np.array_equal(nm[in1], nm[in2]):
                    ok = False
                else:
                    in1 -= 1
                    in2 += 1
                    continue
                break
            if ok:
                lines.append(i + 1)
    return lines


# Part 1

col_before = 0
row_before = 0

for pattern in patterns:
    m = np.array([list(row) for row in pattern.split("\n")])
    cols = process_grid(m, axis=1)
    rows = process_grid(m)
    row_before += sum(rows)
    col_before += sum(cols)

print(col_before + 100 * row_before)

# Part 2

col_before = 0
row_before = 0

for pi, pattern in enumerate(patterns):
    m = np.array([list(row) for row in pattern.split("\n")])
    cols = process_grid(m, axis=1)
    rows = process_grid(m)
    initial = (cols, rows)
    for idx, t in np.ndenumerate(m):
        nm = m.copy()
        nm[idx[0]][idx[1]] = "." if t == "#" else "#"
        ncols = process_grid(nm, axis=1)
        nrows = process_grid(nm)
        new = (ncols, nrows)
        changecol = sum(x for x in new[0] if x not in initial[0])
        changerow = sum(x for x in new[1] if x not in initial[1])
        if changecol > 0 or changerow > 0:
            col_before += changecol
            row_before += changerow
        else:
            continue
        break

print(col_before + 100 * row_before)
