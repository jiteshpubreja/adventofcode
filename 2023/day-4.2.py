import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

cards = []

for line in data:
  card = {}
  card["id"] = int(line.split(":")[0].split()[1].strip())
  card["winning_numbers"] = line.split(":")[1].split("|")[0].strip().split()
  card["my_numbers"] = line.split(":")[1].split("|")[1].strip().split()
  card["copies"] = 1
  cards.append(card)

for i,card in enumerate(cards):
  score = 0
  for number in card["my_numbers"]:
    if number in card["winning_numbers"]:
      score += 1
  for r in range(i+1,i+score+1):
    cards[r]["copies"] += cards[i]["copies"]

answer = sum([card["copies"] for card in cards])

print(answer)