import re
from collections import Counter

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [list(map(int,list(x.strip()))) for x in inpf.read().split("\n") if x.strip()]

basin_map = [[-1 for y in range(len(data[0]))] for x in range(len(data))]

count = 0
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
      count = count + 1
      basin_map[i][j] = count
    if col == 9:
      basin_map[i][j] = 0

total = sum([x.count(-1) for x in basin_map])
while total > 0:
  for i,row in enumerate(basin_map):
    for j,col in enumerate(row):
      possible_values = []
      if i > 0:
        if basin_map[i-1][j] > 0 and col < 0:
          possible_values.append(basin_map[i-1][j])
      if i < len(basin_map) - 1:
        if basin_map[i+1][j] > 0 and col < 0:
          possible_values.append(basin_map[i+1][j])
      if j > 0:
        if basin_map[i][j-1] > 0 and col < 0:
          possible_values.append(basin_map[i][j-1])
      if j < len(row) - 1:
        if basin_map[i][j+1] > 0 and col < 0:
          possible_values.append(basin_map[i][j+1])
      if(len(list(set(possible_values)))) > 1:
        print("error",possible_values)
      elif len(possible_values):
        basin_map[i][j] = possible_values[0]

    total = sum([x.count(-1) for x in basin_map])
counter = Counter([x for d in basin_map for x in d if x > 0])

answer = 1
for x,n in counter.most_common(3):
  answer = answer * n
print(answer)