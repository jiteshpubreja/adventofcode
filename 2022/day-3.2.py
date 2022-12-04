import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def get_priority(item:str) -> int:
  res = ord(item.lower()) - ord("a") + 1
  if item.isupper():
    res += 26
  return res

answer = 0

for x in chunks(data,3):
  for a in list(set(x[0])):
    if a in list(set(x[1])) and a in list(set(x[2])):
      answer += get_priority(a)

print(answer)