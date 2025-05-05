#!/usr/bin/python


def parse(inp):

  return tuple(tuple(map(int, line.split())) for line in inp)


def derive(seq):

  return tuple(map(int.__rsub__, seq, seq[1:]))


def extrapolate(seq, prev=False):

  if not any(seq):
    return 0

  else:
    if prev:
      return seq[0] - extrapolate(derive(seq), prev)
    else:
      return seq[-1] + extrapolate(derive(seq), prev)


def part_1(data):

  return sum(map(extrapolate, data))


def part_2(data):

  return sum(map(extrapolate, data, [True] * len(data)))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

