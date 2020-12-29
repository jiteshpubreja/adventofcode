import os

md = ""

md += "## All the Advent of Code Challenges solved till date.\n"
md += "For more information visit [Advent of Code](https://adventofcode.com/)\n\n"


years = [x for x in os.listdir(".") if os.path.isdir(x) and not x.startswith(".")]
totalStars = 0

for y in years:
    md += f"* [{y}]({y}) - ({len(os.listdir(y))} ⭐️)\n"
    totalStars += len(os.listdir(y))
    for d in sorted(os.listdir(y)):
        name = d.split(".")[0].title().replace("-"," ") + " Part " + d.split(".")[1]
        md += f"  * [{name}]({y}/{d})\n"

md += f"\n{totalStars} ⭐️"

with open("README.md","w",encoding="utf-8") as out:
    out.write(md)
