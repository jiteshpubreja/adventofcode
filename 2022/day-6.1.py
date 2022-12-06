import re

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()


for i in range(len(data) - 3):
  if len(set(data[i:i+4])) == 4:
    break
print(i + 4)