def getInputAsArray():
  with open('aoc2') as my_file:
    return my_file.readlines()

def main():
  inputs = getInputAsArray()
  correct = 0
  for element in inputs:
    policy_and_password = element.split(": ")
    policy = policy_and_password[0]
    password = policy_and_password[1]

    bounds_and_char = policy.split(" ")
    bounds = bounds_and_char[0]
    policy_char = bounds_and_char[1]

    lower_and_upper_bounds = bounds.split("-")
    lower_bound = int(lower_and_upper_bounds[0])
    upper_bound = int(lower_and_upper_bounds[1])

    if lower_bound <= password.count(policy_char) <= upper_bound:
      correct += 1

  print(correct)

if __name__ == '__main__':
  main()
