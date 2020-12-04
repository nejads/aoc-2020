def getInputAsArray():
  with open('aoc31') as my_file:
    return my_file.readlines()

def main():
  inputs = getInputAsArray()
  trees = 0
  for i in range(len(inputs)):
    row = inputs[i].strip() * (i+1)
    if row[i * 3] == '#':
      trees += 1
  print(trees)


if __name__ == '__main__':
  main()
