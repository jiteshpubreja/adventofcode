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

colors = []
for x in bags:
  if "shiny gold" in bags[x]:
    colors.append(x)

retry = True

while retry:
  retry = False
  for x in colors.copy():
    for y in bags:
      if x in bags[y] and y not in colors:
        colors.append(y)
        retry = True

print(len(colors))