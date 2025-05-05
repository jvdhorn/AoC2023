#!/usr/bin/python


def parse(inp):

  graph = dict()
  pipes = {'|': (1j, -1j),
           '-': (-1, 1),
           'L': (-1j, 1),
           'J': (-1j, -1),
           '7': (-1, 1j),
           'F': (1, 1j),
           '.': (0, 0),
           'S': (-1, 1, -1j, 1j)}

  for j, row in enumerate(inp):
    for i, char in enumerate(row.strip()):
      pos = complex(i, j)
      if char == 'S': S = pos
      graph[pos] = frozenset(pos+x for x in pipes.get(char))

  graph[S] = frozenset({x for x in graph[S] if S in graph.get(x,set())})

  return graph, S


def find_loop(graph, start):

  loop = [start, set(graph[start]).pop()]

  while loop[-1] != loop[0]:
    loop.append((set(graph[loop[-1]]) - {loop[-2]}).pop())

  return loop[:-1]


def part_1(data):

  loop = find_loop(*data)

  return len(loop) // 2


def part_2(data):

  loop  = find_loop(*data)
  lefts = set()
  turns = 0

  for curr, nxt, nxt2 in zip(loop, loop[1:] + loop[:1], loop[2:] + loop[:2]):
    drc, drc2 = nxt - curr, nxt2 - nxt
    if   drc == 1:
      lefts |= {curr - 1j, nxt - 1j}
      if   drc2 == -1j: turns += 1
      elif drc2 ==  1j: turns -= 1
    elif drc == -1:
      lefts |= {curr + 1j, nxt + 1j}
      if   drc2 ==  1j: turns += 1
      elif drc2 == -1j: turns -= 1
    elif drc == 1j:
      lefts |= {curr + 1, nxt + 1}
      if   drc2 ==  1: turns += 1
      elif drc2 == -1: turns -= 1
    elif drc == -1j:
      lefts |= {curr - 1, nxt - 1}
      if   drc2 == -1: turns += 1
      elif drc2 ==  1: turns -= 1

  lefts &= set(data[0])
  lefts -= set(loop)
  unass  = set(data[0]) - set(loop) - lefts
  queue  = lefts.copy()

  while queue:
    curr   = queue.pop()
    nxt    = {curr+1, curr-1, curr+1j, curr-1j} & unass
    unass -= nxt
    queue |= nxt
    lefts |= nxt

  lefts &= set(data[0])
  rights = set(data[0]) - set(loop) - lefts

  return len(lefts if turns > 0 else rights)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

