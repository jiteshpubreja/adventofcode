import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [[y.strip() for y in x.strip().split("|")] for x in inpf.read().split("\n") if x.strip()]


total = 0

for s,d in data:
  segments = {}
  digits = []
  for t in s.split(" "):
    if t.strip():
      digits.append("".join(sorted(t)))
  segments[1] = [x for x in digits if len(x) == 2][0]
  segments[7] = [x for x in digits if len(x) == 3][0]
  segments[4] = [x for x in digits if len(x) == 4][0]
  segments[8] = [x for x in digits if len(x) == 7][0]
  segments[3] = [x for x in digits if len(x) == 5 and len(set(segments[7]).union(x)) == 5][0]
  segments[9] = [x for x in digits if len(x) == 6 and len(set(x) - set(segments[3]).union(set(segments[4]))) == 0][0]
  segments[6] = [x for x in digits if len(x) == 6 and len(set(segments[8]) - set(x).union(set(segments[1]))) == 0][0]
  for x in segments.values():
    if x in digits:
      del digits[digits.index(x)]
  segments[0] = [x for x in digits if len(x) == 6 and len(set(segments[8]) - set(x)) == 1][0]
  segments[5] = [x for x in digits if len(x) == 5 and len(set(x) - set(segments[4])) == 2][0]
  segments[2] = [x for x in digits if len(x) == 5 and len(set(x) - set(segments[4])) == 3][0]
  reverse_segments = {y:x for x,y in segments.items()}
  num = ""
  for t in d.split(" "):
    num += str(reverse_segments["".join(sorted(t.strip()))])
  total += int(num)


print(total)