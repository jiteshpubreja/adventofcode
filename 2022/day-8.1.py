import re

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

grid = [list(map(int,x)) for x in data]

visibility_map = [[False for x in y] for y in grid]

def get_values(grid,r,c,reverse=False,ttype="row"):
  if ttype=="row":
    if reverse:
      return grid[r][:c][::-1]
    return grid[r][c+1:]
  if ttype=="col":
    if reverse:
      return [x[c] for i,x in enumerate(grid) if i < r][::-1]
    return [x[c] for i,x in enumerate(grid) if i > r]

def compare_current(grid,r,c):
  visible = False
  visible = visible or grid[r][c] > max(get_values(grid,r,c,True,"row"))
  visible = visible or grid[r][c] > max(get_values(grid,r,c,False,"row"))
  visible = visible or grid[r][c] > max(get_values(grid,r,c,True,"col"))
  visible = visible or grid[r][c] > max(get_values(grid,r,c,False,"col"))
  return visible

for r,col in enumerate(grid):
  for c,cell in enumerate(col):
    if r == 0 or c == 0 or r == len(grid) - 1 or c == len(col) - 1:
      visibility_map[r][c] = True
    else:
      visibility_map[r][c] = compare_current(grid,r,c)

flat_visibility_map = [x for y in visibility_map for x in y]

answer = flat_visibility_map.count(True)

print(answer)