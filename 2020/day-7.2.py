import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

data = [x.strip() for x in data if x.strip()]

bags = {}

for x in data:
  parent = re.sub(r"bag[s]?","",x.split("contain")[0].strip()).strip()
  children = {}
  for y in re.findall(r"\d+ .+? bag[s]?",x):
    temp_name = re.sub(r"\d+|bag[s]?","",y).strip()
    temp_quantity = int(str(re.match(r"\d+",y)[0]))
    children[temp_name] = temp_quantity
  bags[parent] = children


count = 0
pending = []
pending.extend(["shiny gold"])
while pending:
  current = pending.pop()
  for x in bags[current]:
    pending.extend([x]*bags[current][x])
    count += bags[current][x]
print(count)