from pprint import pprint
import copy

def get_seats():
  with open('aoc11') as my_file:
    return list(map(lambda x: list(x.strip()), my_file.readlines()))


def find_adjacent(x,y, lst):
  adj_lst = []
  if x>0 and y>0:
    adj_lst.append(lst[x-1][y-1])

  if x>0:
    adj_lst.append(lst[x-1][y])

  if x>0 and y<len(lst[x])-1:
    adj_lst.append(lst[x-1][y+1])

  if y>0:
    adj_lst.append(lst[x][y-1])

  if y<len(lst[x])-1:
    adj_lst.append(lst[x][y+1])

  if x<len(lst)-1 and y>0:
    adj_lst.append(lst[x+1][y-1])

  if x < len(lst)-1:
    adj_lst.append(lst[x+1][y])

  if x<len(lst)-1 and y<len(lst[x])-1:
    adj_lst.append(lst[x+1][y+1])
  return adj_lst

def no_occupied_adjacent(x,y,lst):
  return find_adjacent(x,y,lst).count('#') == 0

def four_or_more_adjacent_occupied(x,y,lst):
  return find_adjacent(x,y,lst).count('#') >= 4

def iterate(lst):
  init_lst = copy.deepcopy(lst)
  for x in range(len(lst)):
    for y in range(len(lst[x])):
      if lst[x][y] == 'L' and no_occupied_adjacent(x, y, init_lst):
        lst[x][y] = '#'
      if lst[x][y] == '#' and four_or_more_adjacent_occupied(x, y, init_lst):
        lst[x][y] = 'L'
  return init_lst, lst

def count_seats(lst):
  seat = 0
  for x in lst:
    for y in x:
      if y == '#':
        seat += 1
  return seat

def find_occupied_seats():
  init_lst, lst = iterate(get_seats())
  while init_lst != lst:
    init_lst, lst = iterate(lst)
  return count_seats(lst)


def main():
  print("Day11, part1: " + str(find_occupied_seats()))

if __name__ == '__main__':
  main()
