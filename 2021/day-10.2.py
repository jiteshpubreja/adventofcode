import re
from collections import deque

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().strip().split("\n")

points_map = {
  "(": 1,
  "[": 2,
  "{": 3,
  "<": 4,
}

points = []

for chunk in data:
  stack = deque()
  score = 0

  valid = True

  for x in chunk:
    if x in points_map.keys():
      stack.append(x)
    elif x in [")","]","}",">"]:
      last = stack.pop()
      if (last == "(" and x != ")") or (last == "[" and x != "]") or (last == "{" and x != "}") or (last == "<" and x != ">"):
        valid = False
        break

  while len(stack) > 0:
    last = stack.pop()
    score *= 5
    score += points_map.get(last,0)

  if score and valid:
    points.append(score)


print(sorted(points)[len(points)//2])
