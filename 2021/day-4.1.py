import re

data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = [x for x in inpf.read().split("\n\n") if x.strip()]

sequence = [int(x.strip()) for x in data[0].split(",")]
boards = []
for x in data[1:]:
  boards.append([[int(w.strip()) for w in z if w.strip()] for z in [y.split(" ") for y in x.split("\n") if y.strip()]])

def markBoard(board,num):
  for i,y in enumerate(board):
    if num in y:
      board[i][y.index(num)] = "A"
  return board

def checkBoard(board):
  for y in board:
    if y.count("A") == len(y):
      return True
    for i in range(len(board)):
      cols = [x[i] for x in board]
      if cols.count("A") == len(cols):
        return True
  return False 

best_board = None
calling_seq = None

for s in sequence:
  for i,x in enumerate(boards):
    boards[i] = markBoard(x,s)
    if checkBoard(x):
      best_board = x
      calling_seq = s
      break
  if best_board:
    break

numbers = sum([sum([n for n in a if n != "A"]) for a in best_board])
print(numbers*calling_seq)