import re
from functools import reduce

with open("input.txt",encoding="utf-8") as inpf:
  time, distance = inpf.read().split("\n")

time = list(map(int,re.split("\s+",re.split(":\s+",time)[1])))
distance = list(map(int,re.split("\s+",re.split(":\s+",distance)[1])))

total_wins = []

for t,d in zip(time,distance):
  wins = 0
  for x in range(t):
    if x*(t-x) > d:
      wins += 1
  total_wins.append(wins)

print(reduce(lambda a,b : a*b, total_wins))