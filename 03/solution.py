#!/usr/bin/python


def parse(inp):

  inp     = ''.join(inp)
  symbols = dict()
  numbers = dict()

  for i, line in enumerate(inp.split()):
    for j, char in enumerate(line):
      if not char.isdigit() and char != '.':
        symbols[complex(i,j)] = char

  for symbol in set(symbols.values()):
    inp = inp.replace(symbol, '.')

  for i, line in enumerate(inp.split()):
    j = -1
    k = 0

    for number in filter(None, line.split('.')):
      j = line.find(number, j+k+1)
      k = len(number)
      numbers[complex(i,j)] = number

  return symbols, numbers


def part_1(data):

  symbols, numbers = data
  radius = {-1-1j, -1, -1+1j, -1j, 0, 1j, 1-1j, 1, 1+1j}
  result = 0

  for pos, number in numbers.items():
    extent = {pos+1j*x+r for x in range(len(number)) for r in radius}
    if extent & set(symbols):
      result += int(number)

  return result


def part_2(data):

  symbols, numbers = data
  radius = {-1-1j, -1, -1+1j, -1j, 0, 1j, 1-1j, 1, 1+1j}
  result = 0
  gears  = dict()

  for pos, number in numbers.items():
    extent = {pos+1j*x+r for x in range(len(number)) for r in radius}
    common = extent & set(symbols)

    for com in common:
      if symbols[com] == '*':
        gears[com] = gears.get(com,[]) + [number]

  for vals in gears.values():
    if len(vals) == 2:
      result += int(vals[0]) * int(vals[1])

  return result


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

