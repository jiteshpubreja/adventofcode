import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [list(x) for x in inpf.read().split("\n")]

dataYes = set()

def check_xmas(a,b,c,d):
  word = data[a[0]][a[1]]+data[b[0]][b[1]]+data[c[0]][c[1]]+data[d[0]][d[1]]
  if word in ["XMAS","SAMX"]:
    dataYes.add(str(a)+str(b)+str(c)+str(d))
    return True
  return False

def check_rows():
  for i in range(len(data)):
    for j in range(len(data[i])-3):
      check_xmas((i,j),(i,j+1),(i,j+2),(i,j+3))

def check_cols():  
  for i in range(len(data)-3):
    for j in range(len(data[i])):
      check_xmas((i,j),(i+1,j),(i+2,j),(i+3,j))

def check_right_dia():
  for i in range(len(data)-3):
    for j in range(len(data[i])-3):
      check_xmas((i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3))

def check_left_dia():
  for i in range(len(data)-3):
    for j in range(3,len(data[i])):
      check_xmas((i,j),(i+1,j-1),(i+2,j-2),(i+3,j-3))

check_rows()
check_cols()
check_right_dia()
check_left_dia()
answer = len(dataYes)

print(answer)