from shapely import Polygon

with open("day-18.txt", "r") as f:
    input_data = f.read().strip()


def calculate_area(moves):

    inc = {
        # LEFT
        ((-1, 0), (0, 1)): 0.75,
        ((-1, 0), (0, -1)): 0.25,
        # RIGHT
        ((1, 0), (0, 1)): 0.25,
        ((1, 0), (0, -1)): 0.75,
        # UP
        ((0, 1), (-1, 0)): 0.25,
        ((0, 1), (1, 0)): 0.75,
        # DOWN
        ((0, -1), (-1, 0)): 0.75,
        ((0, -1), (1, 0)): 0.25,
    }

    x = 0
    y = 0
    coords = [(x, y)]
    directions = []
    for d, l in moves:
        if d == "L":
            x -= l
            d = (-1, 0)
        elif d == "R":
            x += l
            d = (1, 0)
        elif d == "U":
            y += l
            d = (0, 1)
        elif d == "D":
            y -= l
            d = (0, -1)
        coords.append((x, y))
        directions.append(d)

    directions.append(directions[0])

    acc = 0
    for i in range(1, len(directions)):
        d1 = directions[i - 1]
        d2 = directions[i]
        plus = inc[(d1, d2)]
        acc += plus

    p = Polygon(coords)

    a = p.area + acc + (p.length-len(coords)+1) * 0.5

    return int(a)


# Part 1
moves = []
for line in input_data.split("\n"):
    d, l, _ = line.split(" ")
    moves.append((d,int(l)))

print(calculate_area(moves))

# Part 2

D = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}

moves = []
for line in input_data.split("\n"):
    c = line.split(" ")[2][1:-1]
    l = int(c[1:6],16)
    d = D[c[-1]]
    moves.append((d,l))

print(calculate_area(moves))