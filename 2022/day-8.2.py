import re

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

grid = [list(map(int,x)) for x in data]

scenic_score_map = [[None for x in y] for y in grid]

def get_values(grid,r,c,reverse=False,ttype="row"):
  if ttype=="row":
    if reverse:
      return grid[r][:c][::-1]
    return grid[r][c+1:]
  if ttype=="col":
    if reverse:
      return [x[c] for i,x in enumerate(grid) if i < r][::-1]
    return [x[c] for i,x in enumerate(grid) if i > r]

def get_upto(val,vals):
  new_vals = []
  for x in vals:
    new_vals.append(x)
    if val <= x:
      break
  return new_vals

def compare_current(grid,r,c):
  visible = 1
  visible = visible * len(get_upto(grid[r][c],get_values(grid,r,c,True,"row")))
  visible = visible * len(get_upto(grid[r][c],get_values(grid,r,c,False,"row")))
  visible = visible * len(get_upto(grid[r][c],get_values(grid,r,c,True,"col")))
  visible = visible * len(get_upto(grid[r][c],get_values(grid,r,c,False,"col")))
  return visible

for r,col in enumerate(grid):
  for c,cell in enumerate(col):
    if r == 0 or c == 0 or r == len(grid) - 1 or c == len(col) - 1:
      scenic_score_map[r][c] = 0
    else:
      scenic_score_map[r][c] = compare_current(grid,r,c)

flat_scenic_score_map = [x for y in scenic_score_map for x in y]

answer = max(flat_scenic_score_map)

print(answer)
