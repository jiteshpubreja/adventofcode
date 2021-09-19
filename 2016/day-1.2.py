import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split(",")

data = [x.strip() for x in data if x.strip()]

turns = {
  "NR":"E",
  "NL":"W",
  "ER":"S",
  "EL":"N",
  "SR":"W",
  "SL":"E",
  "WR":"N",
  "WL":"S",
}

currentposition = "N"
x = 0
y = 0

visited = []

found = None

for d in data:
  newposition = turns[currentposition+d[:1]]
  if newposition == "W":
    for t in range(1,int(d[1:])+1):
      if (x-t,y) not in visited:
        visited.append((x-t,y))
      else:
        visited.append((x-t,y))
        found = found if found else (x-t,y)
        break
    x = x - int(d[1:])
  if newposition == "E":
    for t in range(1,int(d[1:])+1):
      if (x+t,y) not in visited:
        visited.append((x+t,y))
      else:
        visited.append((x+t,y))
        found = found if found else (x-t,y)
        break
    x = x + int(d[1:])
  if newposition == "N":
    for t in range(1,int(d[1:])+1):
      if (x,y+t) not in visited:
        visited.append((x,y+t))
      else:
        visited.append((x,y+t))
        found = found if found else (x-t,y)
        break
    y = y + int(d[1:])
  if newposition == "S":
    for t in range(1,int(d[1:])+1):
      if (x,y-t) not in visited:
        visited.append((x,y-t))
      else:
        visited.append((x,y-t))
        found = found if found else (x-t,y)
        break
    y = y - int(d[1:])
  currentposition = newposition

x,y = found
print(abs(x)+abs(y))