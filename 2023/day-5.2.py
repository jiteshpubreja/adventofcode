import re
from multiprocessing import Process, Manager

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n\n")

raw_seeds = [int(x.strip()) for x in data.pop(0).split(":")[1].split()]

seeds = []

MAX_CAP = 50000000

while raw_seeds:
  start = raw_seeds.pop(0)
  count = raw_seeds.pop(0)
  while count > MAX_CAP:
    seeds.append(range(start,start+MAX_CAP))
    start += MAX_CAP
    count -= MAX_CAP
  seeds.append(range(start,start+count))

maps = {}

for m in data:
  md = m.split("\n")
  mapname= md.pop(0).split()[0]
  source = mapname.split("-to-")[0]
  destination = mapname.split("-to-")[1]
  mappings = [list(map(int,x.split())) for x in md]
  maps[source] = {
    "source":source,
    "destination":destination,
    "mappings":mappings
  }

def find_values(source,value):
  for m in maps[source]["mappings"]:
    if value in range(m[1],m[1]+m[2]):
      return m[0] + value - m[1]
  return value

seq = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]


def find_min(range,q):
  answer = None
  for s in range:
    ans = s
    for sq in seq:
      ans = find_values(sq,ans)
    answer = min(answer,ans) if answer != None else ans
  q.append(answer)

with Manager() as manager:
  processes = []

  q = manager.list()
  for sr in seeds:
    processes.append(
      Process(target=find_min,args=(sr,q))
    )

  for p in processes:
    p.start()
  for p in processes:
    p.join()
  
  print(min(q))
