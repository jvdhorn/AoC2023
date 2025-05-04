#!/usr/bin/python


def parse(inp):

  return [(line[:5], int(line[5:])) for line in inp]


class Key(object):

  def __init__(self, inp):

    self.hand   = ['23456789TJQKA'.find(c) for c in inp[0]]
    self.counts = self._counts()

  def _counts(self):

    return sorted(map(self.hand.count, self.hand), reverse=True)

  def __lt__(self, other):

    if self.counts != other.counts:
      return self.counts < other.counts

    else:
      return self.hand < other.hand


class Key2(object):

  def __init__(self, inp):

    self.hand   = ['J23456789TQKA'.find(c) for c in inp[0]]
    self.counts = self._counts()

  def _counts(self):

    c = sorted(map(self.hand.count, set(filter(None, self.hand))), reverse=True)
    c = c or [0]
    c[0] += self.hand.count(0)

    return c

  def __lt__(self, other):

    if self.counts != other.counts:
      return self.counts < other.counts

    else:
      return self.hand < other.hand


def part_1(data):

  return sum((r+1) * h[1] for r, h in enumerate(sorted(data, key=Key)))


def part_2(data):

  return sum((r+1) * h[1] for r, h in enumerate(sorted(data, key=Key2)))


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

