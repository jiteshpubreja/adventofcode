import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()

data = data.split("\n\n")
data = [len(set(x.replace("\n",""))) for x in data]
print(sum(data))
