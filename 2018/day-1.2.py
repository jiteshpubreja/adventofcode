import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

data = [int(x.strip()) for x in data if x.strip()]
current = 0
visited = []
found = False
while not found:
  for x in data:
    current += x
    if current in visited:
      found = True
      break
    else:
      visited.append(current)
print(current)