import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

answer = 0

def range_compare(range1:list,range2:list)->bool:
  contains = True
  for x in range1:
    if x not in range2:
      contains = False
  return contains

for d in data:
  a,b,x,y = map(int,[i for j in d.split(",") for i in j.split("-")])
  range1 = list(range(a,b+1))
  range2 = list(range(x,y+1))
  if range_compare(range1,range2) or range_compare(range2,range1):
    answer += 1
print(answer)