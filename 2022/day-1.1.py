import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n\n")

answer = max([sum(map(int,x.split("\n"))) for x in data])

print(answer)