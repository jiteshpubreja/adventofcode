import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

data = [int(x.strip()) for x in data if x.strip()]
count = 0

for i in range(3,len(data)):
  if sum(data[i-2:i+1]) > sum(data[i-3:i]):
    count += 1

print(count)