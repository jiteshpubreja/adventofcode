import re
from functools import reduce

data = None

list1 = []
list2 = []

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")
  list1 = sorted(map(lambda l: int(l.split()[0]),data))
  list2 = sorted(map(lambda l: int(l.split()[-1]),data))

answer = sum([x*list2.count(x) for x in list1])

print(answer)