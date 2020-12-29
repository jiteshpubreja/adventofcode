
data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read()

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
  print(len(passports) - invalid)