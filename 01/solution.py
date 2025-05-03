#!/usr/bin/python


def parse(inp):

  return inp.readlines()


def part_1(data):

  digits = [''.join(filter(str.isdigit, line)) for line in data]
  total  = sum(int('0'+i[:1]+i[-1:]) for i in digits)

  return total


def part_2(data):

  lookup  = {d:d for d in '123456789'}
  lookup.update(
    {'one'  : '1',
     'two'  : '2',
     'three': '3',
     'four' : '4',
     'five' : '5',
     'six'  : '6',
     'seven': '7',
     'eight': '8',
     'nine' : '9'}
  )
  total = 0

  for line in data:
    first  = min(filter(line.__contains__, lookup), key=line.find)
    last   = max(filter(line.__contains__, lookup), key=line.rfind)
    total += int(lookup[first]+lookup[last])

  return total


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

