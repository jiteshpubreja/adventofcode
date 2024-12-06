import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n\n")

rules = list(map(lambda x: list(map(int,x.split("|"))),data[0].strip().split("\n")))

updates = list(map(lambda x: list(map(int,x.split(","))),data[1].strip().split("\n")))

def check_update(update):
  applicable_rules = list(filter(lambda x:x[0] in update and x[1] in update,rules))
  for rule in applicable_rules:
    if update.index(rule[0]) > update.index(rule[1]):
      return 0
  return update[len(update)//2]

answer = sum([check_update(u) for u in updates])

print(answer)