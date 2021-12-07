import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [x for x in inpf.read().split("\n") if x.strip()]

bit_size = 0

for x in data:
  bit_size = max(len(x),bit_size)

oxygen = data.copy()
co2 = data.copy()

i = 0
while(len(oxygen)>1):
  temp = [x[i] for x in oxygen]
  if temp.count("1") == temp.count("0"):
    oxygen = [x for x in oxygen if x[i] == "1"]
  elif temp.count("1") > temp.count("0"):
    oxygen = [x for x in oxygen if x[i] == "1"]
  else:
    oxygen = [x for x in oxygen if x[i] == "0"]
  i += 1

i = 0
while(len(co2)>1):
  temp = [x[i] for x in co2]
  if temp.count("1") == temp.count("0"):
    co2 = [x for x in co2 if x[i] == "0"]
  elif temp.count("1") > temp.count("0"):
    co2 = [x for x in co2 if x[i] == "0"]
  else:
    co2 = [x for x in co2 if x[i] == "1"]
  i += 1


if len(oxygen) == len(co2):
  print(int(oxygen[0],2)*int(co2[0],2))