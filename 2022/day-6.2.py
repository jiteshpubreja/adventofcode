import re

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()


for i in range(len(data) - 13):
  if len(set(data[i:i+14])) == 14:
    break
print(i + 14)