import re

with open("input.txt",encoding="utf-8") as inpf:
  data = inpf.read().split("\n")


def process_input(data):
  results = []
  for i in range(len(data)):
    if data[i].startswith("$"):
      results.append({
        "cmd":data[i][1:].strip(),
        "response":[]
      })
    else:
      results[-1]["response"].append(data[i])
  return results

def process_files(structured_input):
  tree = {}
  current_marker = []
  for i in range(len(structured_input)):
    cmd = structured_input[i]["cmd"].split(" ")
    if len(cmd) > 1:
      cmd,param = cmd
    else:
      cmd = cmd[0]
    response = [x.split(" ") for x in structured_input[i]["response"]]
    if cmd == "cd":
      if param == "/":
        current_marker = ["/"]
      elif param == "..":
        current_marker.pop()
      else:
        current_marker.append(param)
    elif cmd == "ls":
      key = "/".join(current_marker).replace("//","/")
      for rsp in response:
        new_key = f"{key}/{rsp[1]}".replace("//","/")
        tree[new_key] = rsp[0]
  return tree
def calculate_size(tree):
  sizes =  {}
  for d in [x for x in tree if tree[x] == "dir"]:
    sizes[d] = sum(map(int,[tree[x] for x in tree if (x.startswith(f"{d}/")) and tree[x] != "dir" ]))
  sizes["/"] = sum(map(int,[tree[x] for x in tree if x.count("/") == 1 and tree[x] != "dir" ]))
  sizes["/"] += sum([sizes[x] for x in sizes if x.count("/") == 1 and x != "/"])
  return sizes

structured_input = process_input(data)
tree = process_files(structured_input)

size_tree = calculate_size(tree)

max_system_size = 70000000
update_size = 30000000

free_space = max_system_size - size_tree["/"]
space_required = update_size - free_space

filtered_size = {x:size_tree[x] for x in size_tree if size_tree[x] >= space_required}

answer = min(filtered_size.values())

print(answer)

