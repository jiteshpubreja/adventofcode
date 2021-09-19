import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

data = [int(x.strip()) for x in data if x.strip()]
print(sum(data))