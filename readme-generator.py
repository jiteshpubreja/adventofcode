import os

md = ""

md += "## All the Advent of Code Challenges solved till date.\n"
md += "For more information visit [Advent of Code](https://adventofcode.com/)\n\n"


years = [x for x in os.listdir(".") if os.path.isdir(x) and not x.startswith(".")]
totalStars = 0

for y in sorted(years):
    md += f"* [{y}]({y}) - ({len(os.listdir(y))} ⭐️) - [🔗](https://adventofcode.com/{y}/)\n"
    totalStars += len(os.listdir(y))
    for d in sorted(os.listdir(y),key=lambda x : float(x.split("-")[1].split(".py")[0])):
        link = f"https://adventofcode.com/{y}/" + d.split(".")[0].replace("-","/")
        name = d.split(".")[0].title().replace("-"," ") + " Part " + d.split(".")[1]
        link += "#part2" if d.split(".")[1] == "2" else ""
        md += f"  * [{name}]({y}/{d}) - [🔗]({link})\n"

md += f"\n{totalStars} ⭐️"

with open("README.md","w",encoding="utf-8") as out:
    out.write(md)
