from itertools import chain

def get_file_content():
  with open('aoc6') as my_file:
    return my_file.read()

def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))

def anyone_answers(answer):
  return set(flatten(answer))

def everyone_answers(answer):
  flatten_answer = flatten(answer)
  return set([r for r in flatten_answer if flatten_answer.count(r) == len(answer)])

def count_anyone_answers():
  groups = get_file_content().split("\n\n")
  person_answers = map(lambda g: g.split("\n"), groups)
  answer_group_set = map(lambda answers: anyone_answers(answers), person_answers)
  answer_counts = map(lambda answer_set: len(answer_set), answer_group_set)
  return sum(list(answer_counts))

def count_everyone_answers():
  groups = get_file_content().split("\n\n")
  person_answers = map(lambda g: g.split("\n"), groups)
  answer_group = map(lambda answers: everyone_answers(answers), person_answers)
  answer_counts = map(lambda answer_set: len(answer_set), answer_group)
  return sum(list(answer_counts))

def main():
  print("Day6, part1: " + str(count_anyone_answers()))
  print("Day6, part2: " + str(count_everyone_answers()))

if __name__ == '__main__':
  main()
