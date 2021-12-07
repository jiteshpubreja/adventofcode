import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

data = [x.split(" ") for x in data if x.strip()]
data = [(x,int(y)) for x,y in data]

pos = 0
depth = 0

for x,y in data:
  if x == "forward":
    pos += y
  elif x == "up":
    depth -= y
  elif x == "down":
    depth += y


print(pos*depth)