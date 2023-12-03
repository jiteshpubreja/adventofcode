import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

grid = [[cell for cell in line] for line in data]

total = 0

m = len(grid)
n = len(grid[0])

all_gears = {}

for i in range(m):
  gears = set()
  num = 0
  for j in range(n+1):
    if j<n and grid[i][j].isdigit():
      char = grid[i][j]
      num = num*10 + int(char)
      for x in [-1,0,1]:
        for y in [-1,0,1]:
          if 0 <= i + x < n and 0 <= j + y < m:
            if grid[i+x][j+y]=='*':
              gears.add((i+x, j+y))
    elif num:
      for gear in gears:
        all_gears[gear] = all_gears.get(gear,[])
        all_gears[gear].append(num)
      num = 0
      gears = set()

for gear in all_gears.values():
  if(len(gear) == 2):
    total += gear[0]*gear[1]

print(total)