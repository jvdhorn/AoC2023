#!/usr/bin/python


def parse(inp):

  state = set()
  walls = set()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      if   col == '#': walls.add(complex(j, i))
      elif col == 'O': state.add(complex(j, i))
    walls.add(complex( -1, i))
    walls.add(complex(j+1, i))
  walls |= {complex(x,  -1) for x in range(j+1)}
  walls |= {complex(x, i+1) for x in range(j+1)}

  return state, walls


def move(state, walls, drc):

  state = set(state)
  key   = lambda x: -(x.imag * drc.imag + x.real * drc.real)

  for pos in sorted(state, key=key):
    state.remove(pos)
    nxt = pos + drc
    while nxt not in walls and nxt not in state:
      pos = nxt
      nxt = pos + drc
    state.add(pos)

  return state


def get_score(state, walls):

  zero  = max(i.imag for i in walls)
  score = sum(int(zero - i.imag) for i in state)

  return score


def part_1(data):

  state, walls = data
  state = move(state, walls, -1j)

  return get_score(state, walls)


def part_2(data):

  state, walls = data
  state  = frozenset(state)
  turn   = -1j
  seen   = dict()
  scores = []

  while (state, turn) not in seen:
    seen[state, turn] = len(scores)
    scores.append(get_score(state, walls))
    state  = frozenset(move(state, walls, turn))
    turn  *= -1j

  target = 1000000000
  first  = seen[state, turn]
  cycle  = len(scores) - first

  return scores[first + (4 * target - len(scores)) % cycle]


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

