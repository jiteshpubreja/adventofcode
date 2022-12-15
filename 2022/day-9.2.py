import re

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

inputs = [d.split(" ") for d in data  if d.strip()]

mover = {
  "L" : lambda x : [x[0]-1,x[1]],
  "R" : lambda x : [x[0]+1,x[1]],
  "U" : lambda x : [x[0],x[1]+1],
  "D" : lambda x : [x[0],x[1]-1]
}

def calculate_visited(n,inputs):
  rope = [[0,0] for _ in range(n)]
  visited = set()
  for direction,steps in inputs:
    for _ in range(int(steps)):
      rope[0] = mover[direction](rope[0])

      for i in range(1,n):
        dx = rope[i-1][0] - rope[i][0]
        dy = rope[i-1][1] - rope[i][1]
        if abs(dx) > 1 or abs(dy) > 1:
          rope[i][0] += dx/abs(dx) if dx else 0
          rope[i][1] += dy/abs(dy) if dy else 0

      visited.add(tuple(rope[-1]))  

  return len(visited)

answer = calculate_visited(10,inputs)

print(answer)