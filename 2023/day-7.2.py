import re
from collections import Counter
from functools import cmp_to_key

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

cards_rank = { "A" : 13, "K" : 12, "Q" : 11, "T" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2, "J" : 1}
hands_rank = {"5" : 7, "14" : 6, "23" : 5, "113" : 4, "122" : 3, "1112" : 2, "11111" : 1}

card_bets = [{"card":x.split()[0].strip(),"bet":int(x.split()[1].strip())} for x in data]

def get_cards_rank(card):
  return [cards_rank[x] for x in card["card"]]

def get_hand_rank(card):
  counter = Counter(card["card"])
  to_comp = card["card"]
  most_common = Counter(card["card"]).most_common(5)
  if len(counter) > 1:
    while most_common[0][0] == "J":
      most_common.pop(0)
    to_comp = to_comp.replace("J",most_common[0][0])
  return hands_rank["".join(map(str,sorted(list(Counter(to_comp).values()))))]

def card_sorter(a,b):
  a_rank = get_hand_rank(a)
  b_rank = get_hand_rank(b)
  if a_rank != b_rank:
    return a_rank - b_rank
  
  a_rank = get_cards_rank(a)
  b_rank = get_cards_rank(b)

  while a_rank[0] == b_rank[0]:
    a_rank.pop(0)
    b_rank.pop(0)
  return a_rank[0] - b_rank[0]
  
card_bets.sort(key=cmp_to_key(card_sorter))

answer = 0

for i,c in enumerate(card_bets):
  answer += (i+1)*c["bet"]

print(answer)