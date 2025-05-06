#!/usr/bin/python


def parse(inp):

  inp   = inp.read().split('\n\n')
  grids = set()

  for g in inp:
    grid = set()
    for i, row in enumerate(g.splitlines()):
      for j, col in enumerate(row.strip()):
        if col == '#': grid.add(complex(j, i))
    grids.add(frozenset(grid))

  return grids


def find_reflection(grid, diff = 0):

  reals  = set(int(i.real) for i in grid)
  imags  = set(int(i.imag) for i in grid)
  result = set()

  for i in reals - {max(reals)}:
    i += 0.5
    width = min(i, max(reals) - i)
    iden = {complex(j.real - i, j.imag) for j in grid if abs(j.real - i) <= width}
    refl = {complex(i - j.real, j.imag) for j in grid if abs(i - j.real) <= width}
    if diff in (len(iden-refl), len(refl-iden)): result.add(i)

  for i in imags - {max(imags)}:
    i += 0.5
    width = min(i, max(imags) - i)
    iden = {complex(j.real, j.imag - i) for j in grid if abs(j.imag - i) <= width}
    refl = {complex(j.real, i - j.imag) for j in grid if abs(i - j.imag) <= width}
    if diff in (len(iden-refl), len(refl-iden)): result.add(i * 1j)

  return result


def part_1(data):

  result = 0

  for grid in data:
    refl = find_reflection(grid).pop()
    if refl.real:
      result += int(refl.real + 0.5)
    elif refl.imag:
      result += int(refl.imag + 0.5) * 100

  return result


def part_2(data):

  result = 0

  for grid in data:
    refl = find_reflection(grid, 1).pop()
    if refl.real:
      result += int(refl.real + 0.5)
    elif refl.imag:
      result += int(refl.imag + 0.5) * 100

  return result


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

