import math

iinput = ["....#..#.......#........#....#.", "..##.#.#.#...................#.", "....#.#.##..#....#......#......", ".........#.#......##.....#.....", "..........#.###.##...##........", "#....#.#.......##.....#..#.....", "#...........#.#...#..#..##.##..", "......##.............#.....#...", "..##..........###..#.#..##.....", "...........#........#......##..", "..##...........##..............", "..#......###.#.....#.#.#.......", "..#..#..#..........#.#....#....", ".#.....##......................", "...#...##..#...#.........#..##.", ".#......#..#..#...#......#.##..", "..##.##.......#..#.....#..#...#", "..............#..#..#...#......", "...#...#....##.....#...#...#...", "......................#...#....", ".......#......#...#..##...#.#..", "##......#..#.....#....#.....#..", "....#.#.##.#.#....#............", "#.....##.............#.........", "..........#...........#.#.....#", "...#...##....#.#........#..#...", "................#..#.##.##....#", "......#...#...##...##....#.....", "##....#..#..#...#..#...........", "#..................#...#.#..#..", "....##....##.#....#..#......#..", ".....#...........#.........##..", "..#..............#.........#..#", "......##....................#..", "..#.....###...####...#...#.##..", "#..#.#......#.....#.......#.#..", "##.#.........######........#...", "..#....###...#.#..............#", ".....#..............#.........#", "....#......#..#.........#...#..", ".....###.....#.###.......###...", "#.#..#.....#....##...#........#", "..##....#..#.........#...#.#...", "..#..##.............#....#.#.#.", "..##.#..#.#.#.........##.......", "#.#..#.........#..............#", "#..#.........###.......#.#..#.#", ".............#...#....#......#.", "..........#.#...##.###.....#.#.", "..#.....#......................", ".......#......###.#.......#....", "....#....#.........#...###.#.#.", ".#.............#............#..", "....#..#.............#.#....#..", "....#.....#...#...##.#.........", "..#...#...#..................#.", "........#....#.....#...........", ".....##.......#...#.#..#..#....", "...#............#..#.#.........", "......................#........", "....#......#.....#.#....#......", ".....#..#.........#.........##.", "...............#.....#....##...", "...#.#.#...#..#...........#....", ".#....###......##...#.#.#.#....", ".....#...#....####....##.......", "..#......#..#.....##.#...#.....", "...#.##..#....#..##.....#......", "..#......#...#...##.....#...#..", "......#.....#........#.........", "..#.#....#..............##....#", "..#...#......##............#...", ".##.#.......#.......#......#..#", "...##.##...#.....#.......#..#..", "......##..#....#.......#.......", ".....#..#..#.#.....#.....#...##", "##.#...#.#.#.....#...#.#.#.##.#", "...................###...#..#..", ".#.....##.#......#........#....", ".##...##.#..........#...#....#.", "......#..............#.#......#", "...#.......#..#...........#....", ".###...#............##..#...##.", "##..#.#.........#............#.", "#...#.#......#.##...........#.#", ".#.#...#........#......##......", "....#...#...#.....#...#....#...", "...##...........##.........#...", ".........#...#..###............", "..#........#...............#...", ".............#....#.#..........", "........#......#.#.......#....#", ".................#....##.#.##..", "..#...##........#..............", "#..#........#...#....#.........", "......#.#.....#.....#..###.#..#", "....#............#...#.#.#.....", "............#..........#...#...", "..........#....##.#.........#..", "..............#...#...#..#.....", "#......#....#..##....#......##.", "...#....#.................#....", ".#.##.............#...#....##..", "....#..#.........#..#....#....#", "..#.....##..#......#.#..#......", "..#..#.....#........#...#..#..#", ".........##.#.##.#.......#....#", "..#.......##.##...#.....#.....#", ".............##...#...........#", "..#......#..#....#...#..#.##...", "....#........#......#.........#", ".......#........#..#.#.#..##..#", "..#......#...........##...#....", ".....#..#.#...#..............##", ".#..#......#......#........#..#", "...##...............#....#.....", ".......#...#.......##..#.......", ".....#....#...#...#..#.....#.#.", "...#.........#.....#...........", "...#.....###....#....#...#...#.", "#..#.....#.........#.........#.", ".................#.#.....#....#", "...........#..........#..#.....", "........#.#....#...#..#.....###", "#............................#.", "..##..#..#...##.........#......", "......##....#.#...#.........#..", "......#..##.#......#..#.....#..", "...#.......##....#.#....#......", ".....#........#...#............", "#.......#...#.........#......#.", "......#......#....#..#.........", "..#.#........#..#......#....#..", ".#..#.#..........##....###.#..#", "...#....#.##..#...#....#.......", "..#.....#......#.###.......#...", "..............................#", ".....#..#...#...........#......", ".##...#....##....#.#.#.#....#.#", ".#...#....#...#........#.......", "....#............#...##..#.....", "....##..#....#....#.....#....##", ".............#..##.#.#.#.......", "#.......#.#.#.......#..#..#....", "#..#...........#.......###..#..", ".#..##.#.....#........#........", "..#.#.......#............#..#..", "...........#..#............##.#", ".....#.......#.....#..#.##.#..#", "......#......##.....##.........", "..##.#..#.#..#..#..............", ".....#.............##...#.#.##.", ".#......##.#..........#........", "..#..#.........#.....#.#.#.....", "..#.....#.......#.....#..#.....", "#.#.#........#.#...#....#..#...", ".#.#.......#............#....#.", "......#..................#....#", ".#...#...#.....#.#..........#..", ".#..##....####...........#.#...", "..##.....#...#.#....#....#.....", "#.....................#....#.#.", "###..###.#.#...........#.....##", "......#......#..........#......", "...#......#.##.....#......###.#", ".............#..#.#...........#", "..#.............#.#..#.....#...", "...#...............#....##...##", "........#.................#....", "#..###.....#.......##.#......##", "....#.#..............#.........", "#..........#.....#..##...#.....", "................#...#..#....#..", "..#...#....##..........#.#.....", "......#........##......#..#...#", "...#....#..#.....#.......#...#.", ".#.....#..#...#..###....#......", "....#.........#....#.#.#.....#.", "#.#....#...#....#.....#..##....", ".......#..#..#..........#...#..", "..#.#..#.....##.#.#............", "..#....#.....#..##..#..#.#..#..", "..#.##.#...........#...#..#....", ".........#........#...#........", "..#.#.#.......##.........#.##..", "#.#..........#.#...#..#......##", ".#..#....................#.#...", ".##......#................#...#", "..##.#######......#....#.......", "....#...##.#....#.#............", ".##....#...##.......#...#..#...", "...........#...#...#...#..#....", "#...#.....#.......#....#.....#.", ".............#.................", "........#.#.......#...#.#.#....", "..............#............#.#.", "......#......##..#.......#....#", "##...#..................#......", ".....#......###.....#.......#.#", ".....#.#............#.#........", "..#.#..#............#....#.#...", "##.#.###.#.#.#..#......#.......", "...##........#..#.....#.#.#..#.", "##......#.##.....####..#.......", "............#...#..#...#..#....", "...#..#................##.#..#.", ".#....#.#...........##.#.#...#.", "####..#...........#.......###..", ".......#.................#.....", ".......#....#.......##....#....", "..#.........#...#....#.........", "..........#..#...#.#...##..#...", "....##..........#.........##...", "#.........##..#.#..#.......#...", ".#...........#....#...#...#.#..", "....#..#.....#...##....#.#....#", ".#....#.....#......#..##.##.#.#", "#......#..#.......##...........", "...#..#...#.#.................#", "......#.......##....##.#......#", "....#....#.#.#.....#....#....#.", "..#..........#.##...##..#......", "...#..#........#....#.#..#....#", "##.......#........#..........#.", ".#........#.......#...#..##...#", "..#..#..##..#...........#...###", "..#......#..........#..##......", ".#.....#..#.#...#...#.........#", "#.#......##....................", "#...#.....##...........#.......", "........#...#....#.......##....", "...#.##...#....#....#..#..#..#.", "...#..#......##....#..#..##....", "#...#..........#.#.............", "##..#........##.....#.........#", ".....#......#.#...###..#.......", "#..##.#..#.###...........##..#.", ".....#....#..........#.......#.", "##.........##.#................", "....#.........#............##..", ".......#........#......#..#..##", ".#...#...##..#....#..#.........", ".............#...#.#........#..", "......#..#...#..#.###..#.......", "........##.#..#.#..#..#........", "#.##..#..#..........#...##..###", ".##...#............#.#...##..#.", "................#....##.#...#..", "#.................#..........#.", "...#..#..#.....................", "..#...##.#.#...................", ".....#...#.......#............#", "..#..#.........#..##.#..#.#...#", ".....#.#.....#.#.......#.....#.", "..................#..#....#.#..", "..#.....###.##.......##....#.#.", "..#......##.......#....##.#....", "....#...................#..##.#", ".......#....#.##.#.......#....#", "..#...#......#..#...###....#.#.", "..#..#.#....#...........#.....#", ".....#..#..#.......#........#..", "......#.##.#......#...........#", "#...#....#.#..##.##..#..##.....", "#...##....#.#...##........#....", "..##............#.#.#..........", "....#.....#.#..#.......#..#....", "#..#.#.....#..#..##...#..##....", "...##........#...........#...#.", ".####......#..##.........#.#...", ".......#.......................", ".................#....#..#.....", ".........##......###...........", ".##......#.#.#....#.#...#..###.", "....#......##.###.#.#..#.......", "..........#.......##......##..#", "...........#.......#..##.......", ".....###..#..............##....", "........##..#.#.#......#....#..", "#....#.........................", "...........#...............##..", "......#.................#......", ".....#...#..##...##...#...#....", "..........#.#...##.####......#.", "..#.#.....##....#...........#..", "..........#....#..#....##...#..", ".#.......#..##...#...#.....#...", "...##....#.#......##...##....#.", "#.......#.......#.##.#...#.#...", "#...#..................#......#", "..#.......#...............#..##", "#.....#..................#....#", ".##.....#.....#......####.....#", "..#........#...#.#........#...#", "..##.....#....#...#...........#", "..#..#.....##..#.##...#........", "..........###..#....##.....#...", "...#...#....#.##.#...#.#.......", "..##......#.......#.......##...", "............#............#.....", ".##....#.........#.............", "....#....#....#........##...#.#", ".......##......................", "..........#.#.................#", "......##.#...#.........#.....#.", "..#...#......#..#.............#", "..........###.#..#.#...#..#..#.", "#..#.#..#....##...#...#.#...#..", ".#........##...#......#.##.....", "...###.#...##..............##..", "#.#.#...#...#..#....#.#..#.....", ".#.#.##..#....#......#.#.......", "...#..#.#....##...........#..#.", ".....##..##......#.#...........", "......#.....#....####....#.....", ".#.#.#...#..#..#...........#...", ".....#......................#..", ".........#.........#.###.##....", ".....#......##..........#......", "..#...........##...........#...", "..............#.........#.....#", "..#....#..#...#...##.#.........", ".#.#.#....#..........#........."]

size = len(iinput[0])
rows = len(iinput)

def treeFinder(right,down):
  trees = 0
  currentRow = 0
  currentCol = 0
  while currentRow < rows - 1:
    currentCol = (currentCol + right) % size
    currentRow += down
    if iinput[currentRow][currentCol] == "#":
      trees += 1
  return trees

tries = [[1,1], [3,1], [5,1], [7,1], [1,2]]

print(math.prod([treeFinder(x[0],x[1]) for x in tries]))