def get_list_of_numbers():
  with open('aoc9') as my_file:
    return list(map(lambda x: int(x), my_file.readlines()))

def num_is_sum_of_two(num, lst):
  for itm in lst:
   if num-itm in lst:
     return True
  return False

def find_answers():
  answers = []
  preambles = 25
  initial_list = get_list_of_numbers()
  #part1
  for i in range(len(initial_list)-preambles):
    num = initial_list[preambles+i]
    lst = initial_list[i:preambles+i]
    if not num_is_sum_of_two(num, lst):
      answers.append(num)
  #part2
  for i in range(len(initial_list)):
    for j in range(len(initial_list)):
      if answers[0] == sum(initial_list[i:j]):
        answers.append(min(initial_list[i:j]) + max(initial_list[i:j]))
        return answers

def main():
  print("Day9, part1: " + str(find_answers()[0]))
  print("Day9, part2: " + str(find_answers()[1]))


if __name__ == '__main__':
  main()
