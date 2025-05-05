#!/usr/bin/python


def parse(inp):

  result = []

  for line in inp:
    pattern, groups = line.split()
    pattern = tuple(map('.?#'.find, pattern))
    while '..' in pattern: pattern = pattern.replace('..', '.')
    groups  = tuple(map(int, groups.split(',')))
    result.append((pattern, groups))

  return result


def count_perm(pattern, groups, cache=dict()):

  if (pattern, groups) in cache:
    return cache[pattern, groups]

  p, g = pattern, groups

  if not groups:
    result = (2 not in pattern)

  else:
    lim    = sum(groups) + len(groups) - 1
    curr   = groups[0]
    groups = groups[1:]
    result = 0
    while len(pattern) >= lim:
      if 0 not in pattern[:curr] and 2 not in pattern[curr:curr+1]:
        result += count_perm(pattern[curr+1:], groups)
      if pattern[0] == 2: break
      else              : pattern = pattern[1:]

  cache[p, g] = result

  return result


def part_1(data):

  result = 0

  for pattern, groups in data:
    result += count_perm(pattern, groups)

  return result


def part_2(data):

  result = 0

  for pattern, groups in data:
    pattern = ((pattern + (1,)) * 5)[:-1]
    groups  = groups * 5
    result += count_perm(pattern, groups)

  return result


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

