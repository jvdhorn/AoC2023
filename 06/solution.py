#!/usr/bin/python


def parse(inp):

  return tuple(zip(*(map(int, line.split()[1:]) for line in inp)))


def part_1(data):

  result = 1

  for time, record in data:
    result *= sum(i * (time-i) > record for i in range(time+1))

  return result


def part_2(data):

  time, record = [int(''.join(map(str, x))) for x in zip(*data)]

  return sum(i * (time-i) > record for i in range(time//2)) * 2 + 1


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

