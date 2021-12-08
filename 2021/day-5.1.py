import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [[y.strip() for y in x.split("->")] for x in inpf.read().split("\n") if x.strip()]

data = [[tuple([int(z) for z in y.split(",")]) for y in x] for x in data]

maxx = max([max([y[0] for y in x]) for x in data])
maxy = max([max([y[1] for y in x]) for x in data])

floor = [[0]*(maxx+1) for x in range(maxy+1)]

for d in data:
  if d[0][0] == d[1][0] or d[0][1] == d[1][1]:
    x1 = min(d[0][0],d[1][0])
    x2 = max(d[0][0],d[1][0])
    y1 = min(d[0][1],d[1][1])
    y2 = max(d[0][1],d[1][1])
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        floor[y][x] += 1

answer = sum([len([g for g in f if g > 1]) for f in floor])
print(answer)