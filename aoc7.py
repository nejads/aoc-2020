import re

def get_file():
  with open('aoc7') as my_file:
    return my_file.readlines()

def find_bags():
  bags = ['shiny gold']
  for bag in bags:
    for line in get_file():
      new_bag = re.split('\sbags\s', line)[0]
      if re.search('\s\d\s'+bag+'\sbag*', line) and new_bag not in bags:
        bags.append(new_bag)
  bags.remove('shiny gold')
  return str(len(bags))

def main():
  print("Day7, part1: " + find_bags())

if __name__ == '__main__':
  main()
