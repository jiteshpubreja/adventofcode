from functools import reduce
import re
import math

num_patt = re.compile(r'\d+')

class Monkey:
  uid:int
  items:list[int]
  operation:str
  test:str
  if_true:int
  if_false:int
  items_held:int

  def __init__(self,initial_monkey:str) -> None:
    state = initial_monkey.split("\n")
    self.uid = int(re.search(num_patt,state[0]).group())
    self.items = [int(x) for x in state[1].split(":")[1].split(",")]
    self.operation = state[2].split("=")[1].strip()
    self.test = int(re.search(num_patt,state[3]).group())
    self.if_true = int(re.search(num_patt,state[4]).group())
    self.if_false = int(re.search(num_patt,state[5]).group())
    self.items_held = 0
  
  def __repr__(self) -> str:
    return str(self.__dict__)


monkeys:dict[str,Monkey] = {}

with open("input.txt",encoding="utf-8") as inpf:
  data = [x.strip() for x in inpf.read().split("\n\n")]

for d in data:
  m = Monkey(d)
  monkeys[m.uid] = m

def operation(operation:str,old:int) -> int:
  result = eval(operation.replace("old",str(old)))
  return result

def play_round(monkeys:dict[str,Monkey]):
  worry_divider = reduce(math.lcm,[monkeys[k].test for k in monkeys])
  for k in monkeys:
    for item in monkeys[k].items:
      monkeys[k].items_held += 1
      worry = operation(monkeys[k].operation,item) % worry_divider
      if worry % monkeys[k].test == 0:
        monkeys[monkeys[k].if_true].items.append(worry)
      else:
        monkeys[monkeys[k].if_false].items.append(worry)
    monkeys[k].items = []
  return monkeys

def get_answer(monkeys):
  for _ in range(10000):
    monkeys = play_round(monkeys)
  return reduce(lambda x,y:x*y,sorted([monkeys[k].items_held for k in monkeys],reverse=True)[:2])

answer = get_answer(monkeys)

print(answer)
