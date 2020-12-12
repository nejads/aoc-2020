import re
from pprint import pprint


def get_operations():
  operations = []
  with open('aoc8') as my_file:
    lines = my_file.readlines()
  for line in lines:
    op_val = line.strip().split(" ")
    operations.append([op_val[0], op_val[1]])
  return operations

def calc_accumulator(operations):
  accumulator = 0
  i = 0
  indexes = []
  indexes.append(i)
  while i < len(operations):

    if operations[i][0] == 'nop':
      i += 1
      if i in indexes and len(indexes) < len(operations):
        return accumulator
      else:
        indexes.append(i)

    if i == len(operations):
      print("Day8, part2: " + str(accumulator))
      return accumulator

    if operations[i][0] == 'acc':
      accumulator += int(operations[i][1])
      i += 1
      if i in indexes and len(indexes) < len(operations):
        return accumulator
      else:
        indexes.append(i)

    if i == len(operations):
      print("Day8, part2: " + str(accumulator))
      return accumulator

    if operations[i][0] == 'jmp':
      i += int(operations[i][1])
      if i in indexes and len(indexes) < len(operations):
        return accumulator
      else:
        indexes.append(i)

    if i == len(operations):
      print("Day8, part2: " + str(accumulator))
      return accumulator


def fix_loop_accumulator():
  operations = get_operations()
  for operation in operations:
    if operation[0] == 'nop':
      operation[0] = 'jmp'
      calc_accumulator(operations)
      operation[0] = 'nop'

    if operation[0] == 'jmp':
      operation[0] = 'nop'
      calc_accumulator(operations)
      operation[0] = 'jmp'


def main():
  print("Day8, part1: " + str(calc_accumulator(get_operations())))
  fix_loop_accumulator()


if __name__ == '__main__':
  main()
