import re
from collections import deque

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

points_map = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137,
}

points = 0

for chunk in data:
  stack = deque()

  for x in chunk:
    if x in ["(","[","{","<"]:
      stack.append(x)
    elif x in points_map.keys():
      last = stack.pop()
      if (last == "(" and x != ")") or (last == "[" and x != "]") or (last == "{" and x != "}") or (last == "<" and x != ">"):
        points += points_map.get(x,0)
        break

print(points)
