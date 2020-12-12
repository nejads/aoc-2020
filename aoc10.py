def get_sorted_list():
  with open('aoc10') as my_file:
    return list(sorted(map(lambda x: int(x), my_file.readlines())))

def find_ones_and_threes():
  lst = get_sorted_list()
  lst.insert(0, 0)  #charging outlet
  lst.append(max(lst)+3)  #build-in adapter
  ones, threes = 0, 0
  for i in range(len(lst)-1):
    jmp = lst[i+1]-lst[i]
    if jmp == 1:
      ones += 1
    if jmp == 3:
      threes += 1
  return ones*threes

def main():
  print("Day10, part1: " + str(find_ones_and_threes()))

if __name__ == '__main__':
  main()
