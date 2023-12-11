import numpy as np

# Part 1

with open("day-06.txt", "r") as f:
    data = f.readlines()

times = [int(t) for t in data[0].split(":")[1].split()]
distances = [int(d) for d in data[1].split(":")[1].split()]

race_data = list(zip(times, distances))


def get_ways(time, record):
    distances = [hold_sec * (time - hold_sec) for hold_sec in range(time)]
    return len([distance for distance in distances if distance > record])


race_ways = [get_ways(time, record) for time, record in race_data]

print(np.prod(race_ways))

# Part 2

time = ""
for t in times:
    time += str(t)
time = int(time)

distance = ""
for d in distances:
    distance += str(d)
distance = int(distance)

print(get_ways(time, distance))
