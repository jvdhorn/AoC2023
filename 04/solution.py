#!/usr/bin/python


def parse(inp):

  data = dict()

  for line in inp:
    colon        = line.find(':')
    n_card       = int(line[5:colon])
    numbers      = line[colon+1:].split('|')
    data[n_card] = tuple(set(map(int, x.split())) for x in numbers)

  return data


def part_1(data):

  result = 0

  for win, own in data.values():
    result += 2 ** len(win&own) // 2

  return result


def part_2(data):

  queue = list(data)
  count = 0
  cache = dict()

  while queue:
    count += 1
    card   = queue.pop()
    if card in cache:
      new = cache[card]
    else:
      new = [card+n for n in range(1,1+len(set.intersection(*data[card])))]
      cache[card] = new

    queue += new

  return count


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

