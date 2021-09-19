import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()

data = [x.strip() for x in list(data) if x.strip()]

total = 0

for i,x in enumerate(data):
  if data[i-1] == data[i]:
    total += int(data[i])

print(total)