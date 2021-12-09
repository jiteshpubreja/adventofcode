import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [[y.strip() for y in x.strip().split("|")] for x in inpf.read().split("\n") if x.strip()]
  digits = [[len(y.strip()) for y in x[1].split(" ") if y.strip()] for x in data]

total = sum([len([y for y in x if y in [2,3,4,7]]) for x in digits])
print(total)