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

for d in data:
  newposition = turns[currentposition+d[:1]]
  if newposition == "W":
    x = x - int(d[1:])
  if newposition == "E":
    x = x + int(d[1:])
  if newposition == "N":
    y = y + int(d[1:])
  if newposition == "S":
    y = y - int(d[1:])
  currentposition = newposition

print(abs(x)+abs(y))