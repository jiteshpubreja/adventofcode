import re

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

inputs = [d.split(" ") for d in data if d.strip()]

instructions = {
  "noop":1,
  "addx":2
}


def cycles_to_check(cycles,inputs):
  total_cycles = 1
  x_reg = 1
  results = {}

  for x in inputs:
    x.append(0)
    for _ in range(instructions[x[0]]):
      if total_cycles in cycles:
        results[total_cycles] = x_reg
      total_cycles += 1
    x_reg += int(x[1])
  return results

answer = sum([x*y for x,y in cycles_to_check(list(range(20,221,40)),inputs).items()])

print(answer)
