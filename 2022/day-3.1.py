import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")


def get_priority(item:str) -> int:
  res = ord(item.lower()) - ord("a") + 1
  if item.isupper():
    res += 26
  return res

answer = 0

for x in data:
  for a in list(set(x[:len(x)//2])):
    if a in list(set(x[len(x)//2:])):
      answer += get_priority(a)

print(answer)