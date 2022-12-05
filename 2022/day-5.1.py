import re

with open("input.txt",encoding="utf-8") as inpf:
  initial_stacks,procedures = inpf.read().split("\n\n")
initial_stack_map = {}
for count in [x.strip() for x in initial_stacks.split("\n")[-1].split(" ") if x.strip()]:
  count = int(count)
  for s in initial_stacks.split("\n")[:-1]:
    value = s[0+(count-1)*4:(count)*4].strip()
    if value:
      initial_stack_map[count] = initial_stack_map.get(count,[])
      initial_stack_map[count].append(value[1:-1])

stacks = {}
for k in initial_stack_map.keys():
  stacks[k] = []
  while initial_stack_map[k]:
    stacks[k].append(initial_stack_map[k].pop())

for p in procedures.split("\n"):
  n,f,t = list(map(int,re.findall(r"\d+",p)))
  for _ in range(n):
    stacks[t].append(stacks[f].pop())

print("".join([x[-1] for x in stacks.values()]))