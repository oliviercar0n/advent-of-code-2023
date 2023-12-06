import numpy as np


SYMBOLS = "*/-@$=%+#&"



def p1(m):
    sum_numbers = 0
    for j in range(0, m.shape[0]):
        i1 = None
        i2 = None
        for i in range(0, m.shape[1]):
            number = None
            if m[j][i].isdigit():
                if i2 is None:
                    i1 = i
                i2 = i
                if i == m.shape[1] - 1:
                    number = int("".join(m[j][i1 : i2 + 1]))
                elif not m[j][i + 1].isdigit():
                    number = int("".join(m[j][i1 : i2 + 1]))
                if number:
                    valid_number = False
                    for y in range(max(j - 1, 0), min(j + 2, m.shape[0])):
                        for x in range(max(i1 - 1, 0), min(i2 + 2, m.shape[1])):
                            cell = m[y][x]
                            if cell in list(SYMBOLS):
                                valid_number = True
                    if valid_number:
                        sum_numbers += number
                    i2 = None
                    i1 = None

    print(f"The sum of the part numbers is {sum_numbers}")

def p2(m):
    raise NotImplementedError




with open("puzzle-input.txt", "r") as f:
    m = np.array([list(row) for row in f.read().split("\n")])


p1(m)