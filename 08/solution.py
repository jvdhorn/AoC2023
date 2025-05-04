#!/usr/bin/python


def parse(inp):

  seq   = tuple(map('LR'.find, next(inp)))[:-1]
  graph = dict()

  next(inp)

  for line in inp:
    a, b, c = ''.join((' '+c)[c.isalpha()] for c in line).split()
    graph[a] = (b,c)

  return seq, graph


def get_gcd(a, b):

  a, b = sorted((a, b))

  while a != b:
    a, b = sorted((b-a, a))

  return a


def get_lcm(a, b):

  return a * b // get_gcd(a, b)


def part_1(data):

  seq, graph = data
  seq        = list(seq)

  curr  = 'AAA'
  steps = 0

  while curr != 'ZZZ':
    curr = graph[curr][seq[0]]
    seq.append(seq.pop(0))
    steps += 1

  return steps


def part_2(data):

  seq, graph = data
  nodes      = [node for node in graph if node.endswith('A')]
  cycles     = set()

  for node in nodes:
    queue = list(seq)
    steps = 0
    while not node.endswith('Z'):
      steps += 1
      node = graph[node][queue[0]]
      queue.append(queue.pop(0))
    cycles.add(steps)

  lcm = 1

  while cycles:
    lcm = get_lcm(lcm, cycles.pop())

  return lcm


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

