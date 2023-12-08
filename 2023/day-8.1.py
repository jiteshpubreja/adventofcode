import re

with open("input.txt",encoding="utf-8") as inpf:
  instructions, maps = inpf.read().split("\n\n")

final_maps = {}

for m in maps.split("\n"):
  key = m.split("=")[0].strip()
  left = m.split("=")[1].strip().split(",")[0].split("(")[1].strip()
  right = m.split("=")[1].strip().split(",")[1].split(")")[0].strip()
  final_maps[key] = {
    "L":left,
    "R":right
  }

start = "AAA"

steps = 0

while start != "ZZZ":
  start = final_maps[start][instructions[steps%len(instructions)]]
  steps += 1

print(steps)