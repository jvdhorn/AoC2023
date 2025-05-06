#!/usr/bin/python


def parse(inp):

  return inp.read().strip().split(',')


def HASH(inp):

  result = 0

  while inp:
    c, *inp = inp
    result  = (result + ord(c)) * 17 % 256

  return result


def part_1(data):

  return sum(map(HASH, data))


def part_2(data):

  boxes = {i:list() for i in range(256)}

  for ins in data:
    label = ''.join(filter(str.isalpha, ins))
    ins   = ins.strip(label)
    box   = boxes[HASH(label)]
    pos   = [b for b in box if label in b]

    if ins[0] == '-' and pos:
      box.remove(pos[0])

    elif ins[0] == '=':
      new = (label, int(ins[1:]))

      if pos:
        box[box.index(pos[0])] = new
      else:
        box.append(new)

  result = 0

  for i, box in boxes.items():
    result += (i+1) * sum((j+1) * b[1] for j, b in enumerate(box))

  return result


if __name__ == '__main__':

  with open(0) as inp:
    data = parse(inp)

  sol1 = part_1(data)
  print(sol1)

  sol2 = part_2(data)
  print(sol2)

