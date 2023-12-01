import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

answer = sum(map(lambda t: int(t[0]+t[-1]),[reduce(lambda x,y : x+y if re.match(r'[0-9]+',y) else x,z,'') for z in data]))

print(answer)