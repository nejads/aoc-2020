def getInputAsArray():
  with open('aoc31') as my_file:
    return my_file.readlines()

def main():
  inputs = getInputAsArray()
  slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
  rows = list(map(lambda s: s.strip() * len(inputs), inputs))
  total = 1
  for (dx, dy) in slopes:
    x, y, trees = 0, 0, 0
    while y < len(rows):
      trees += rows[y][x] ==  '#'
      x = (x + dx) % len(rows[y])
      y = (y + dy)
    total *= trees
  print(total)

if __name__ == '__main__':
  main()
