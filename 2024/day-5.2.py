import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n\n")

rules = list(map(lambda x: list(map(int,x.split("|"))),data[0].strip().split("\n")))

updates = list(map(lambda x: list(map(int,x.split(","))),data[1].strip().split("\n")))

fixed_updates = []

def check_update(update):
  applicable_rules = list(filter(lambda x:x[0] in update and x[1] in update,rules))
  for rule in applicable_rules:
    if update.index(rule[0]) > update.index(rule[1]):
      return 0
  return update[len(update)//2]

def check_update_incorrect(update):
  applicable_rules = list(filter(lambda x:x[0] in update and x[1] in update,rules))
  incorrect = False
  for rule in applicable_rules:
    if update.index(rule[0]) > update.index(rule[1]):
      incorrect = True
  return incorrect

def fix_updates(update):
  applicable_rules = list(filter(lambda x:x[0] in update and x[1] in update,rules))
  while check_update_incorrect(update):
    for rule in applicable_rules:
      index1 = update.index(rule[0])
      index2 = update.index(rule[1])
      if index1 > index2:
        update[index1],update[index2] = update[index2],update[index1]
  return update


for u in updates:
  if check_update_incorrect(u):
    fixed_updates.append(fix_updates(u))


answer = sum([check_update(u) for u in fixed_updates])

print(answer)