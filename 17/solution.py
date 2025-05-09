#!/usr/bin/python


def parse(inp):

  grid = dict()

  for i, row in enumerate(inp):
    for j, col in enumerate(row.strip()):
      grid[complex(j,i)] = int(col)

  return grid


def solve(maze, pos, end, least=1, most=3):

  queue = {0:[(pos,pos)]}
  valid = set(maze)
  seen  = set()

  while pos != end:
    steps    = min(queue)
    path     = queue[steps].pop()
    drc, pos = path

    if not queue[steps]: queue.pop(steps)
    if path in seen    : continue
    else               : seen.add(path)

    opts = {(pos+(i*j), i*(i.real+i.imag),
             steps + sum(maze[pos+(i*k)] for k in range(1,j+1)))
                    for i in {-1, 1, -1j, +1j} - {drc, -drc}
                    for j in range(least, most+1) if pos+(i*j) in valid}

    for opt, drc, cost in opts:
      if cost not in queue: queue[cost] = list()
      queue[cost] += [(drc, opt)]

  return steps


def part_1(data):

  return solve(data, 0, max(data, key=abs))


def part_2(data):

  return solve(data, 0, max(data, key=abs), 4, 10)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

