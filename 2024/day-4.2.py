import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [list(x) for x in inpf.read().split("\n")]

dataYes = set()

def check_xmas(a,b,c,d,e,f):
  word1 = data[a[0]][a[1]]+data[b[0]][b[1]]+data[c[0]][c[1]]
  word2 = data[d[0]][d[1]]+data[e[0]][e[1]]+data[f[0]][f[1]]
  if word1 in ["MAS","SAM"] and word2 in ["MAS","SAM"]:
    dataYes.add(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
    return True
  return False

def check_mas():
  for i in range(len(data)-2):
    for j in range(len(data[i])-2):
      check_xmas((i,j),(i+1,j+1),(i+2,j+2),(i,j+2),(i+1,j+1),(i+2,j))


check_mas()
answer = len(dataYes)

print(answer)