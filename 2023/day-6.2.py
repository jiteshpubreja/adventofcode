import re

with open("input.txt",encoding="utf-8") as inpf:
  time, distance = inpf.read().split("\n")

time = int(re.sub(r"\s+","",re.split(":\s+",time)[1]))
distance = int(re.sub(r"\s+","",re.split(":\s+",distance)[1]))

total_wins = []

win = 0
for x in range(time):
  if x*(time-x) > distance:
    win += 1

print(win)