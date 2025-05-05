#!/usr/bin/python


def parse(inp):

  grid = set()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      if col == '#': grid.add(complex(i,j))

  return grid


def get_distances(data, mult):

  reals = {int(x.real) for x in data}
  imags = {int(x.imag) for x in data}

  r_exp = set(range(min(reals), max(reals)+1)) - reals
  i_exp = set(range(min(imags), max(imags)+1)) - imags

  dist  = dict()

  for i in data:
    for j in data:
      if i != j and (i,j) not in dist and (j,i) not in dist:
        dist[i,j]  = int(abs(i.real - j.real) + abs(i.imag - j.imag))
        dist[i,j] += sum(i.real<x<j.real or j.real<x<i.real for x in r_exp
                     ) * (mult - 1)
        dist[i,j] += sum(i.imag<x<j.imag or j.imag<x<i.imag for x in i_exp
                     ) * (mult - 1)

  return dist


def part_1(data):

  dist = get_distances(data, 2)

  return sum(dist.values())


def part_2(data):

  dist = get_distances(data, 1000000)

  return sum(dist.values())


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

