import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

digits = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

first = [[j[0] for j in list(filter(lambda z: z[1]>-1, sorted(d.items(),key=lambda x:d[x[0]])))] for d in [{d:x.find(d) for d in digits} for x in data]]
last = [[j[0] for j in list(filter(lambda z: z[1]>-1, sorted(d.items(),key=lambda x:d[x[0]])))] for d in [{d:x[::-1].find(d[::-1]) for d in digits} for x in data]]

answer = sum(map(int,[f"{digits.get(x[0])}{digits.get(y[0])}" for x,y in zip(first,last)]))

print(answer)