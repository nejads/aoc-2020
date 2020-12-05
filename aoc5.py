def getInputAsArray():
  with open('aoc5') as my_file:
    return my_file.readlines()

def calculate_id(chars, lower, upper, lower_char, upper_char):
  for char in chars:
    if char == lower_char:
      upper = ((upper - lower) // 2) + lower
    if char == upper_char:
      lower = ((upper - lower) // 2) + lower + 1
  assert upper == lower
  return upper

def calculate_sead_id(seat):
  row = calculate_id(seat[:7], 0, 127, 'F', 'B')
  column = calculate_id(seat[7:], 0, 7, 'L', 'R')
  return row * 8 + column

def diff(lst1, lst2):
  return set(lst1) ^ set(lst2)

def find_missing(lst):
  return [x for x in range(lst[0], lst[-1]+1) if x not in lst]

def main():
  seats = getInputAsArray()
  seat_ids = list(map(lambda seat: calculate_sead_id(seat), seats))
  print("Day5, part1: " + str(max(seat_ids)))
  print("Day5, part2: " + str(find_missing(seat_ids)[0]))

if __name__ == '__main__':
  main()
