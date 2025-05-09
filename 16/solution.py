#!/usr/bin/python


def parse(inp):

  grid = dict()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      item = '/\\|-'.find(col)
      if item >= 0: grid[complex(j,i)] = item

  return grid, complex(j, i)


def trace(inp, start):

  grid, lim = inp
  paths     = {start}
  seen      = set()
  obstacles = {0: {-1j: (1,), 1: (-1j,), 1j: (-1,), -1: (1j,)},
               1: {-1j: (-1,), 1: (1j,), 1j: (1,), -1: (-1j,)},
               2: {-1j: (-1j,), 1: (-1j,1j), 1j: (1j,), -1: (-1j,1j)},
               3: {-1j: (-1,1), 1: (1,), 1j: (-1,1), -1: (-1,)}}

  while paths:
    pos, drc = paths.pop()

    while (pos, drc) not in seen and (
        lim.real >= pos.real >= 0 <= pos.imag <= lim.imag):
      seen.add((pos, drc))

      if pos in grid:
        alts = obstacles[grid[pos]][drc]
        for alt in alts[1:]: paths.add((pos+alt, alt))
        drc = alts[0]

      pos = pos + drc

  return len({pos for pos, drc in seen})


def part_1(data):

  return trace(data, (0,1))


def part_2(data):

  grid, lim = data

  t = {(i, 1j) for i in range(int(lim.real))}
  b = {(i+lim.imag*1j, -1j) for i in range(int(lim.real))}
  l = {(i*1j, 1) for i in range(int(lim.imag))}
  r = {(i*1j+lim.real, -1) for i in range(int(lim.imag))}

  return max(trace(data, start) for start in t|b|l|r)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

