#!/usr/bin/python


def parse(inp):

  inst = []

  for d, x, h in map(str.split, inp):
    inst.append((1j**'RDLU'.find(d) * int(x), int(h.strip('(#)'), 16)))

  return inst


def find_path(inst):

  path = [inst[0]]

  for nxt in inst[1:]+inst[:1]:
    curr  = path[-1]
    drc   = nxt - curr
    path += [curr + (i+1) * drc/abs(drc) for i in range(int(abs(drc)))]

  return path[:-1]


def fill(path):

  inner  = set()

  for i, j in zip(path, path[1:] + path[:1]):
    drc = j - i
    if   drc ==  1 : inner |= {i-1j, j-1j}
    elif drc == -1 : inner |= {i+1j, j+1j}
    elif drc ==  1j: inner |= {i+1 , j+1 }
    elif drc == -1j: inner |= {i-1 , j-1 }

  path   = set(path)
  inner -= path
  queue  = inner.copy()

  while queue:
    curr   = queue.pop()
    nb     = {curr+1, curr-1, curr+1j, curr-1j} - path - inner
    inner |= nb
    queue |= nb

  return inner | path


def is_clockwise(path):

  turns = 0

  for i, j, k in zip(path, path[1:] + path[:1], path[2:] + path[:2]):
    drc_a = (j - i) / abs(j - i)
    drc_b = (k - j) / abs(k - j)
    if   drc_a ==  1 :
      if   drc_b == -1j: turns += 1
      elif drc_b ==  1j: turns -= 1
    elif drc_a == -1 :
      if   drc_b ==  1j: turns += 1
      elif drc_b == -1j: turns -= 1
    elif drc_a ==  1j:
      if   drc_b ==  1 : turns += 1
      elif drc_b == -1 : turns -= 1
    elif drc_a == -1j:
      if   drc_b == -1 : turns += 1
      elif drc_b ==  1 : turns -= 1

  return turns > 0


def get_bounds(path):

  reals = set()
  imags = set()

  for i, j in zip(path, path[1:] + path[:1]):
    drc = (j - i) / abs(j - i)
    if   drc ==  1 : imags.add(i.imag + 0.5)
    elif drc == -1 : imags.add(i.imag - 0.5)
    elif drc ==  1j: reals.add(i.real - 0.5)
    elif drc == -1j: reals.add(i.real + 0.5)

  return sorted(reals), sorted(imags)


def get_super(pos, bounds):

  x = next(i - 1 for i, j in enumerate(bounds[0]) if j > pos.real)
  y = next(i - 1 for i, j in enumerate(bounds[1]) if j > pos.imag)

  return complex(x, y)


def split_path(path):

  alts = []

  for i, pos in enumerate(path):
    if pos in path[i+1:]:
      alt = path[i:path.index(pos, i+1)]
      path[i:path.index(pos, i+1)] = []
      for p in split_path(alt): alts.append(p)

  alts.append(path)

  return alts


def get_area(pos, bounds):

  x = bounds[0][int(pos.real)+1] - bounds[0][int(pos.real)]
  y = bounds[1][int(pos.imag)+1] - bounds[1][int(pos.imag)]

  return int(x * y)


def part_1(data):

  path = find_path([sum(j for j, _ in data[:i]) for i in range(len(data))])
  if not is_clockwise(path): path = path[::-1]
  area = len(fill(path))

  return area


def part_2(data):

  inst   = [h//16*1j**(h%16) for _, h in data]
  path   = [sum(inst[:i]) for i in range(len(inst))]
  if not is_clockwise(path): path = path[::-1]
  bounds = get_bounds(path)
  path   = find_path([get_super(x, bounds) for x in path])

  seen   = set(path)
  paths  = [p for p in split_path(path) if len(p) >= 8]
  for p in paths:
    seen |= fill(p)

  return sum(get_area(pos, bounds) for pos in seen)


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

