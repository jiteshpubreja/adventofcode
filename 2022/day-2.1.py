import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

maps = {
  "A":1,
  "B":2,
  "C":3,
  "X":1,
  "Y":2,
  "Z":3,
}

steps = [list(map(maps.get,x.split(" "))) for x in data]

final_answer = 0

for x,y in steps:
  answer = y
  if x == y:
    answer += 3
  elif (x == 2 and y == 3) or (x==3 and y==1) or (x == 1 and y == 2):
    answer += 6
  final_answer += answer 

print(final_answer)