import re
from functools import reduce

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

def fuzzy_report(report):
  report = list(map(int,report.split()))
  option1 = check_report(report)
  if option1:
    return option1
  for i in range(len(report)):
    fuzz_report = report.copy()
    fuzz_report.pop(i)
    option2 = check_report(fuzz_report)
    if option2:
      return option2
  return option1

def check_report(report):
  inc = all([report[i]<report[i+1] for i in range(len(report)-1)])
  dec = all([report[i]>report[i+1] for i in range(len(report)-1)])

  if not inc and not dec:
    return 0
  for i in range(len(report)-1):
    delta = abs(report[i] - report[i+1])
    if delta not in [1,2,3]:
      return 0
  return 1

answer = sum([fuzzy_report(x) for x in data])

print(answer)