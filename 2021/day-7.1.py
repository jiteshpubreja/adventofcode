import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [int(x.strip()) for x in inpf.read().split(",") if x.strip()]

fuels = {}

for i in range(min(data),max(data)+1):
  fuels[i] = fuels.get(i,0) + sum(abs(x-i) for x in data)
minfuel = min(fuels.values())

print(minfuel)