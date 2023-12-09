import re

with open("input.txt",encoding="utf-8") as inpf:
  data = [list(map(lambda x: int(x.strip()),x.split())) for x in inpf.read().split("\n")]


def predict_next(arr):
  curr = [arr]
  steps = 0
  
  while not all([x == 0 for x in curr[steps]]):
    if len(curr) == steps+1:
      curr.append([])
    for i in range(len(curr[steps])-1):
      curr[steps+1].append(curr[steps][i+1] - curr[steps][i])
    steps += 1
  
  for i in range(steps,0,-1):
    curr[i-1].append(curr[i-1][-1]+curr[i][-1])
  return curr[0][-1]


print(sum([predict_next(x) for x in data]))