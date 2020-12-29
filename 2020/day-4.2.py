import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()

validators = {
  "byr" : lambda x: len(x) == 4 and x.isdigit() and int(x) >= 1920 and int(x) <= 2002,
  "iyr" : lambda x: len(x) == 4 and x.isdigit() and int(x) >= 2010 and int(x) <= 2020,
  "eyr" : lambda x: len(x) == 4 and x.isdigit() and int(x) >= 2020 and int(x) <= 2030,
  "hgt" : lambda x: (x.endswith("in") and x[:-2].isdigit() and int(x[:-2]) >= 59 and int(x[:-2]) <= 76) or (x.endswith("cm") and x[:-2].isdigit() and int(x[:-2]) >= 150 and int(x[:-2]) <= 193),
  "hcl" : lambda x: re.match(r"\#[0-9a-f]{6}",x),
  "ecl" : lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
  "pid" : lambda x: len(x) == 9 and x.isdigit()
}



valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
invalid = 0
if data:
  passports = [x.replace("\n"," ") for x in data.strip().split("\n\n")]
  for p in passports:
    passport = {x.split(":")[0]:x.split(":")[1] for x in p.split(" ")}
    for v in valid_keys:
      if v not in passport:
        invalid += 1
        break
      elif not validators[v](passport[v]):
        invalid += 1
        break
  print(len(passports) - invalid)