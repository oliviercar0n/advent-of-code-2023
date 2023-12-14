import numpy as np


with open("day-14.txt", "r") as f:
    input_data = f.read().strip()

m = np.array([list(row) for row in input_data.split("\n")])

# Part 1
ans = 0
for idx, t in np.ndenumerate(m):
  if t == "O":
     r = idx[0]
     c = idx[1]
     furthest = False
     while furthest == False:
          if m[max(r-1,0)][c] != "." or r == 0:
               furthest=True
               m[idx[0]][c] = "."
               m[r][c] = "O"
               ans += len(m) - r
          else:
              r -= 1

print(ans)
