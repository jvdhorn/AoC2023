#!/usr/bin/python


def parse(inp):

  data = dict()

  for line in inp:
    colon  = line.find(':')
    n_game = int(line[5:colon])
    draws  = []

    for draw in line[colon+1:].split(';'):
      draws.append({j:int(i) for i,j in map(str.split, draw.split(','))})

    data[n_game] = draws

  return data


def part_1(data):

  limits = {'red': 12, 'green': 13, 'blue': 14}
  legal  = []

  for n_game, draws in data.items():
    if all(draw[col]<=limits[col] for draw in draws for col in draw):
      legal.append(n_game)

  return sum(legal)


def part_2(data):

  result = 0

  for n_game, draws in data.items():
    power = 1

    for col in 'red', 'green', 'blue':
      power *= max(draw.get(col, 0) for draw in draws)

    result += power

  return result


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

