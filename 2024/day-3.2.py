import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()

matches = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)",data)

answer = 0

enabled = True

for match in matches:
  if match  == "don't()":
    enabled = False
  elif match == "do()":
    enabled = True
  elif enabled:
    res = re.findall(r"mul\((\d+),(\d+)\)",match).pop()
    answer += int(res[0])*(int(res[1]))

print(answer)