import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

maps = {
  "A":1,
  "B":2,
  "C":3,
  "X":0,
  "Y":3,
  "Z":6,
}

steps = [list(map(maps.get,x.split(" "))) for x in data]

final_answer = 0

for x,y in steps:
  if y == 0:
    answer = x - 1
  elif y == 3:
    answer = x
  elif y == 6:
    answer = x + 1

  if answer == 0:
    answer += 3
  if answer > 3:
    answer -= 3
  answer += y
  final_answer += answer 

print(final_answer)