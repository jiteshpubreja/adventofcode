import re
from functools import reduce

data = None 

position = [-1,-1]
direction = [-1,0]
visits = set()

directions = {
  "[-1, 0]":[0,1],
  "[0, 1]":[1,0],
  "[1, 0]":[0,-1],
  "[0, -1]":[-1,0],
}

with open("input.txt",encoding="utf-8") as inpf:
  data = [list(x) for x in inpf.read().split("\n")]

for x in range(len(data)):
  for y in range(len(data[0])):
    if data[x][y] == "^":
      position = [x,y]
      visits.add(str(position))

while(position[0]+direction[0] in range(len(data)) and position[1]+direction[1] in range(len(data[0]))):
  newposition = [position[0]+direction[0],position[1]+direction[1]]
  if data[newposition[0]][newposition[1]] != "#":
    position = newposition
    visits.add(str(position))
  else:
    direction = directions[str(direction)]


answer = len(visits)

print(answer)