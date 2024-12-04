import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

def check_report(report):
  report = list(map(int,report.split()))
  if sorted(report) != report and sorted(report,reverse=True) != report:
    return 0
  for i in range(len(report)-1):
    delta = abs(report[i] - report[i+1])
    if delta not in [1,2,3]:
      return 0
  return 1

answer = sum([check_report(x) for x in data])

print(answer)