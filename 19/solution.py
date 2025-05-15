#!/usr/bin/python


def parse(inp):

  rules = dict()

  workflows, inps, *_ = inp.read().split('\n\n')

  for rule in workflows.splitlines():
    name = rule[:rule.find('{')]
    rule = sum((tuple(x.split(':'))
                for x in rule.strip(name).strip('{}').split(',')),())
    rules[name] = rule

  rules = simplify(rules)

  inputs = list()

  for line in inps.splitlines():
    inst = dict()
    for sub in line.strip('{}').split(','):
      idx, val = sub.split('=')
      inst[idx] = int(val)
    inputs.append(inst)

  return rules, inputs


def simplify(rules):

  for name, rule in rules.copy().items():
    i = 0
    while len(rule) > 3:
      subrulename = name + str(i)
      i += 1
      rules[subrulename] = rule[-3:]
      rule = rule[:-3] + (subrulename,)
    rules[name] = rule

  return rules


def factory(cond, a, b):

  def func(inp, r):
    comp = {'>': int.__gt__, '<': int.__lt__}
    met  = comp[cond[1]](inp[cond[0]], int(cond[2:]))
    if met: return r[a](inp, r)
    else  : return r[b](inp, r)

  return func


def as_funcs(rules):

  funcs = {name: factory(*rule) for name, rule in rules.items()}

  funcs['A'] = lambda inp, r: True
  funcs['R'] = lambda inp, r: False

  return funcs


def solve_rec(rules, name, ranges):

  if name in 'AR':
    if name == 'R': return 0
    prod = 1
    for i, j in ranges.values(): prod *= max(j - i + 1, 0)
    return prod

  cond, a, b = rules[name]
  key  = cond[0]
  comp = cond[1]
  val  = int(cond[2:])
  rng  = ranges[key]

  if   comp == '<':
    rng_a = (min(rng[0], val-1), min(rng[1], val-1))
    rng_b = (max(rng[0], val  ), max(rng[1], val  ))
  elif comp == '>':
    rng_a = (max(rng[0], val+1), max(rng[1], val+1))
    rng_b = (min(rng[0], val  ), min(rng[1], val  ))

  ranges_a = ranges.copy()
  ranges_b = ranges.copy()
  ranges_a[key] = rng_a
  ranges_b[key] = rng_b

  return solve_rec(rules, a, ranges_a) + solve_rec(rules, b, ranges_b)


def part_1(data):

  rules, inps = data
  rules = as_funcs(rules)

  return sum(x for inp in inps if rules['in'](inp, rules)
             for x in inp.values())


def part_2(data):

  rules, _ = data
  ranges   = {c:(1,4000) for c in 'xmas'}
  result   = solve_rec(rules, 'in', ranges)

  return result


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

