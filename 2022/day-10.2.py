import re

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

inputs = [d.split(" ") for d in data if d.strip()]

instructions = {
  "noop":1,
  "addx":2
}

def cycles_to_check(inputs):
  total_cycles = 1
  x_reg = 1
  crt = []
  for x in inputs:
    x.append(0)
    for _ in range(instructions[x[0]]):
      if (total_cycles-1) % 40 in range(x_reg-1,x_reg+2):
        crt.append("#")
      else:
        crt.append(".")
      total_cycles += 1
    x_reg += int(x[1])
  return crt

answer = cycles_to_check(inputs)

for i,x in enumerate(answer):
  if i % 40 == 0:
    print()
  print(x,end="")
print()