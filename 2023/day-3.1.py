import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

grid = [[cell for cell in line] for line in data]

total = 0

m = len(grid)
n = len(grid[0])

for i in range(m):
  num = 0
  has_part = False
  for j in range(n+1):
    if j<n and grid[i][j].isdigit():
      char = grid[i][j]
      num = num*10 + int(char)
      for x in [-1,0,1]:
        for y in [-1,0,1]:
          if 0 <= i + x < n and 0 <= j + y < m:
            if not grid[i+x][j+y].isdigit() and grid[i+x][j+y] != ".":
              has_part = True
    elif num:
      if has_part:
        total += num
      num = 0
      has_part = False

print(total)