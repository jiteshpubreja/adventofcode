import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [list(map(int,list(x.strip()))) for x in inpf.read().split("\n") if x.strip()]

lowest_points = []

for i,row in enumerate(data):
  for j,col in enumerate(row):
    lowest = True
    if i > 0:
      if data[i-1][j] <= col:
        lowest = False
    if i < len(data) - 1:
      if data[i+1][j] <= col:
        lowest = False
    if j > 0:
      if data[i][j-1] <= col:
        lowest = False
    if j < len(row) - 1:
      if data[i][j+1] <= col:
        lowest = False
    if lowest:
      lowest_points.append(col)
print(sum(lowest_points)+len(lowest_points))