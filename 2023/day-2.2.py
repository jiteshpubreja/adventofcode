data = None

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")

def check_cubes(games_data):

  game_result = { "red":0, "green":0, "blue":0 }
  for game_data in games_data.split(";"):
    for x in game_data.split(","):
      x = x.strip()
      if x:
        cnt,col = x.split()
        game_result[col] = max(int(cnt),game_result[col])
  return game_result["red"] * game_result["green"] * game_result["blue"]

colors = ["red", "green", "blue"]

games = {}

for d in data:
  game_id, games_data = d.split(":")
  game_id = game_id.strip().split(" ")[1].strip()
  games[game_id] = check_cubes(games_data)

answer = sum(games.values())

print(answer)
