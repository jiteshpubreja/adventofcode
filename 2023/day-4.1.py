import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

answer = 0

cards = []

for line in data:
  card = {}
  card["id"] = line.split(":")[0].split()[1].strip()
  card["winning_numbers"] = line.split(":")[1].split("|")[0].strip().split()
  card["my_numbers"] = line.split(":")[1].split("|")[1].strip().split()
  cards.append(card)

for card in cards:
  score = 0
  for number in card["my_numbers"]:
    if number in card["winning_numbers"]:
      score = 1 if score == 0 else score * 2
  answer += score

print(answer)