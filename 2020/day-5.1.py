import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

maxindex = 0

for x in data:
  row = -1
  column = -1
  index = -1
  start = 0
  end = 127
  for y in x[:7]:
    if y == "F":
      end = (start+end) // 2
    elif y == "B":
      start = (start+end+1) // 2
    if start == end:
      row = start
  
  start = 0
  end = 7
  for y in x[7:]:
    if y == "L":
      end = (start+end) // 2
    elif y == "R":
      start = (start+end+1) // 2
    if start == end:
      column = start
  index = row * 8 + column
  if maxindex < index:
    maxindex = index

print(maxindex)
