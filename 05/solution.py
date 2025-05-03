#!/usr/bin/python


def parse(inp):

  seeds = tuple(map(int, next(inp).split()[1:]))
  maps  = dict()

  for line in inp:
    if 'map' in line:
      src, _, dst   = line.split()[0].split('-')
      maps[src,dst] = []
    elif line.strip():
      maps[src,dst].append(tuple(map(int, line.split())))    

  return seeds, maps


class Converter:

  def __init__(self, ranges):

    self._ranges = ranges

  def __call__(self, inp):

    single_inp = isinstance(inp, int)

    if single_inp: inp = [(inp, 1)]

    result = []
    for dst, src, rng in self._ranges:
      queue = []
      for start, end in inp:
        i, j = start, min(src, start+end)
        if j > i: queue.append((i, j-i))
        i, j = max(start, src), min(start+end, src+rng)
        if j > i: result.append((i-src+dst, j-i))
        i, j = max(start, src+rng), start+end
        if j > i: queue.append((i, j-i))
        inp = queue

    result = result + inp

    return result[0][0] if single_inp else result


def part_1(data):

  seeds, maps = data
  converters  = {io:Converter(ranges) for io, ranges in maps.items()}
  best        = 9e999

  for val in seeds:
    src = 'seed'
    while src != 'location':
      dst = next(d for s, d in converters if s==src)
      val = converters[src,dst](val)
      src = dst
    best = min(val, best)

  return best


def part_2(data):

  seeds, maps = data
  converters  = {io:Converter(ranges) for io, ranges in maps.items()}
  best        = 9e999

  for inp in zip(*[iter(seeds)]*2):
    result = [inp]
    src    = 'seed'

    while src != 'location':
      dst    = next(d for s, d in converters if s==src)
      result = converters[src, dst](result)
      src    = dst

    best = min((best, *next(zip(*result))))

  return best


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

