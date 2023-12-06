import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n\n")

seeds = [int(x.strip()) for x in data.pop(0).split(":")[1].split()]

maps = {}

for m in data:
  mp = m.split("\n")
  mapname= mp.pop(0).split()[0]
  source = mapname.split("-to-")[0]
  destination = mapname.split("-to-")[1]
  mappings = [list(map(int,x.split())) for x in mp]
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

answer = None

for s in seeds:
  ans = s
  for sq in seq:
    ans = find_values(sq,ans)
  answer = min(answer,ans) if answer != None else ans
  
print(answer)
  