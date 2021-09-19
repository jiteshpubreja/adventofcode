import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()

data = data.split("\n\n")
data = [x.split("\n") for x in data]
counts = []
for x in data:
  temp = [set(y) for y in x if y]
  settemp = temp[0]
  if len(temp) > 1:
    for y in temp[1:]:
      settemp = settemp & y
  counts.append(len(settemp))
print(sum(counts))