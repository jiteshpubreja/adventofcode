import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [int(x.strip()) for x in inpf.read().split(",") if x.strip()]

timers = {x:0 for x in [0,1,2,3,4,5,6,7,8]}
for i in data:
  timers[i] += 1
for i in range(80):
  timers = {x-1:y for x,y in timers.items()}
  if timers.get(-1,None) is not None:
    timers[6] += timers[-1]
    timers[8] = timers[-1]
    del timers[-1]

print(sum(timers.values()))