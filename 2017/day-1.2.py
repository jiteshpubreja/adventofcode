import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()

data = [x.strip() for x in list(data) if x.strip()]

total = 0

for i in range(0,len(data)//2):
  if data[i] == data[i+len(data)//2]:
    total += int(data[i])*2
  

print(total)