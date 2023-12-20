from shapely import Polygon

with open("day-18.txt", "r") as f:
    input_data = f.read().strip()


def calculate_area(moves):
    x = 0
    y = 0
    coords = [(x, y)]
    directions = []
    for d, l in moves:
        if d == "L":
            x -= l
        elif d == "R":
            x += l
        elif d == "U":
            y += l
        elif d == "D":
            y -= l
        coords.append((x, y))

    p = Polygon(coords)
    a = p.area + p.length//2 + 1

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