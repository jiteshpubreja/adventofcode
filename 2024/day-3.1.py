import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()

matches = re.findall(r"mul\((\d+),(\d+)\)",data)

answer = sum([int(x[0])*int(x[1]) for x in matches])

print(answer)