import re

valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def get_file_content():
  with open('aoc4') as my_file:
    return my_file.read()

def extract_key_value(s):
  return dict(
    map(lambda s: s.split(":"),
      s.replace("\n", " ").split(" ")))


def get_passport_list():
  return map(lambda p: extract_key_value(p), get_file_content().split("\n\n"))

def diff(li1, li2):
  return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def check_present_fields(passport):
  optional_field = 'cid'
  valid_filed_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  dif = diff(list(passport.keys()), valid_filed_names)
  return len(dif) == 0 or (len(dif) == 1 and dif[0] == optional_field)

def find_passport_with_mandatory_fields():
  return filter(lambda p: check_present_fields(p), get_passport_list())

def find_valid_passport():
  filters = [
      lambda p: check_present_fields(p),
      lambda p: 1920 <= int(p['byr']) <= 2002,
      lambda p: 2010 <= int(p['iyr']) <= 2020,
      lambda p: 2020 <= int(p['eyr']) <= 2030,
      lambda p: bool(re.search('((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)$', p['hgt'])),
      lambda p: bool(re.search('#(\d|[a-f]){6}$', p['hcl'])),
      lambda p: len(p['pid']) == 9 and bool(re.search('\d{9}', p['pid'])),
      lambda p: p['ecl'] in valid_eye_color
  ]
  return filter(lambda x: all(f(x) for f in filters), get_passport_list())

def main():
  print("Day4, part1: " + str(len(list(find_passport_with_mandatory_fields()))))
  print("Day4, part2: " + str(len(list(find_valid_passport()))))

if __name__ == '__main__':
  main()
