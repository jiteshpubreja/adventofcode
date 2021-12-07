import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

data = [x.split(" ") for x in data if x.strip()]
data = [(x,int(y)) for x,y in data]

pos = 0
depth = 0
aim = 0

for x,y in data:
  if x == "forward":
    pos += y
    depth += aim*y
  elif x == "up":
    aim -= y
  elif x == "down":
    aim += y


print(pos*depth)