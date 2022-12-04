import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n\n")

sums = [sum(map(int,x.split("\n"))) for x in data]
answer = sum(sorted(sums,reverse=True)[:3])

print(answer)