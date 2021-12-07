import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

data = [int(x.strip()) for x in data if x.strip()]
count = 0

for i in range(1,len(data)):
  if data[i] > data[i-1]:
    count += 1

print(count)