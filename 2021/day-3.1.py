import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [x for x in inpf.read().split("\n") if x.strip()]

bit_size = 0

for x in data:
  bit_size = max(len(x),bit_size)

gamma = ""
epsilon = ""

for i in range(bit_size):
  temp = [x[i] for x in data]
  if temp.count("1") > temp.count("0"):
    gamma += "1"
    epsilon += "0"
  else:
    gamma += "0"
    epsilon += "1"


print(int(gamma,2)*int(epsilon,2))