from collections import defaultdict
from functools import reduce
import numpy as np

input = '3,8,1005,8,324,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,29,1,1107,14,10,1006,0,63,1006,0,71,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,61,1,103,18,10,1006,0,14,1,105,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,94,1006,0,37,1006,0,55,2,1101,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,126,2,1006,12,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,152,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,173,1006,0,51,1006,0,26,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,202,2,8,18,10,1,103,19,10,1,1102,1,10,1006,0,85,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,238,2,1002,8,10,1006,0,41,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,267,2,1108,17,10,2,105,11,10,1006,0,59,1006,0,90,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,304,101,1,9,9,1007,9,993,10,1005,10,15,99,109,646,104,0,104,1,21102,936735777688,1,1,21101,341,0,0,1105,1,445,21101,0,937264173716,1,21101,352,0,0,1106,0,445,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,3245513819,0,1,21102,1,399,0,1105,1,445,21102,1,29086470235,1,21102,410,1,0,1105,1,445,3,10,104,0,104,0,3,10,104,0,104,0,21101,825544712960,0,1,21102,1,433,0,1106,0,445,21102,825460826472,1,1,21101,0,444,0,1106,0,445,99,109,2,22102,1,-1,1,21101,0,40,2,21101,0,476,3,21102,466,1,0,1105,1,509,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,471,472,487,4,0,1001,471,1,471,108,4,471,10,1006,10,503,1101,0,0,471,109,-2,2106,0,0,0,109,4,2101,0,-1,508,1207,-3,0,10,1006,10,526,21101,0,0,-3,21202,-3,1,1,21201,-2,0,2,21101,0,1,3,21101,0,545,0,1105,1,550,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,573,2207,-4,-2,10,1006,10,573,21202,-4,1,-4,1106,0,641,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,0,592,0,1105,1,550,22101,0,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,611,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,633,22101,0,-1,1,21102,633,1,0,105,1,508,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0'

def string_to_dict(value):
  return dict(enumerate([int(i) for i in value.split(',')]))

def check1n2(value, inx, relative_base):
  modes = str(value.get(inx, 0))[:-2][::-1]
  params = []

  for i in range(2):
    if i >= len(modes):
      params.append(value.get(value.get(inx+i+1, 0), 0))
    else:
      if int(modes[i]) == 0:
        params.append(value.get(value.get(inx+i+1, 0), 0))
      elif int(modes[i]) == 1:
        params.append(value.get(inx+i+1, 0))
      elif int(modes[i]) == 2:
        params.append(value.get(value.get(inx+i+1, 0) + relative_base, 0))

  if len(modes) < 3:
    params.append(value.get(inx+3, 0))
  else:
    if int(modes[-1]) == 0:
      params.append(value.get(inx+3, 0))
    elif int(modes[-1]) == 2:
      params.append(value.get(inx+3) + relative_base)

  if int(str(value.get(inx, 0))[-1]) == 1:
    value[params[2]] = params[0] + params[1]
  elif int(str(value.get(inx, 0))[-1]) == 2:
    value[params[2]] = params[0] * params[1]

def check3n4(value, inx, to_input, relative_base):
  modes = str(value.get(inx, 0))[:-2][::-1]
  params = []

  if len(modes) == 0:
    params.append(value.get(inx+1, 0))
  else:
    if int(modes[0]) == 0:
      params.append(value.get(inx+1, 0))
    elif int(modes[0]) == 1:
      params.append(inx+1)
    elif int(modes[0]) == 2:
      params.append(value.get(inx+1, 0) + relative_base)

  if int(str(value.get(inx, 0))[-1]) == 3:
    value[params[0]] = to_input
  elif int(str(value.get(inx, 0))[-1]) == 4:
    return value.get(params[0])

def check5n6(value, inx, relative_base):
  modes = str(value.get(inx, 0))[:-2][::-1]
  params = []

  for i in range(2):
    if i >= len(modes):
      params.append(value.get(value.get(inx+i+1, 0), 0))
    else:
      if int(modes[i]) == 0:
        params.append(value.get(value.get(inx+i+1, 0), 0))
      elif int(modes[i]) == 1:
        params.append(value.get(inx+i+1, 0))
      elif int(modes[i]) == 2:
        params.append(value.get(value.get(inx+i+1, 0) + relative_base, 0))

  if int(str(value.get(inx, 0))[-1]) == 5 and params[0]:
    inx = params[1]
  elif int(str(value.get(inx, 0))[-1]) == 6 and params[0] == 0:
    inx = params[1]
  else:
    inx += 3
  return inx

def check7n8(value, inx, relative_base):
  modes = str(value.get(inx, 0))[:-2][::-1]
  params = []

  for i in range(2):
    if i >= len(modes):
      params.append(value.get(value.get(inx+i+1, 0), 0))
    else:
      if int(modes[i]) == 0:
        params.append(value.get(value.get(inx+i+1, 0), 0))
      elif int(modes[i]) == 1:
        params.append(value.get(inx+i+1, 0))
      elif int(modes[i]) == 2:
        params.append(value.get(value.get(inx+i+1, 0) + relative_base, 0))
  
  if len(modes) < 3:
    params.append(value.get(inx+3, 0))
  else:
    if int(modes[-1]) == 0:
      params.append(value.get(inx+3, 0))
    elif int(modes[-1]) == 2:
      params.append(value.get(inx+3) + relative_base)

  if int(str(value.get(inx, 0))[-1]) == 7:
    value[params[2]] = int(params[0] < params[1])
  elif int(str(value.get(inx, 0))[-1]) == 8:
    value[params[2]] = int(params[0] == params[1])

def check9(value, inx, relative_base):
  modes = str(value.get(inx, 0))[:-2][::-1]
  params = []

  if len(modes) == 0:
    params.append(value.get(inx+1, 0))
  else:
    if int(modes[0]) == 0:
      params.append(value.get(inx+1, 0))
    elif int(modes[0]) == 1:
      params.append(inx+1)
    elif int(modes[0]) == 2:
      params.append(value.get(inx+1, 0) + relative_base)

  return value.get(params[0], 0)

def change_direction(x, y, turn):
  if (x == 1 and turn == 0) or (x == -1 and turn == 1):
    return (0, 1)
  elif (x == 1 and turn == 1) or (x == -1 and turn == 0):
    return (0, -1)
  elif (y == 1 and turn == 0) or (y == -1 and turn == 1):
    return (-1, 0)
  elif (y == 1 and turn == 1) or (y == -1 and turn == 0):
    return (1, 0)

def int_code(value, to_input):
  value = string_to_dict(value)
  inx = 0
  output = 0
  relative_base = 0
  paintorturn = 0

  while(inx < len(value)):
    if value[inx] == 99:
      return output
    else:
      if int(str(value[inx])[-1]) == 1 or int(str(value[inx])[-1]) == 2:
        check1n2(value, inx, relative_base)
        inx += 4

      elif int(str(value[inx])[-1]) == 3 or int(str(value[inx])[-1]) == 4:
        buffer = check3n4(value, inx, to_input, relative_base)
        if buffer or buffer == 0:
          output = buffer
          if not paintorturn % 2:
            yield output
          else:
            to_input = yield output
          paintorturn += 1
        inx += 2

      elif int(str(value[inx])[-1]) == 5 or int(str(value[inx])[-1]) == 6:
        inx = check5n6(value, inx, relative_base)
      
      elif int(str(value[inx])[-1]) == 7 or int(str(value[inx])[-1]) == 8:
        check7n8(value, inx, relative_base)
        inx += 4

      elif int(str(value[inx])[-1]) == 9:
        relative_base += check9(value, inx, relative_base)
        inx += 2

def calculate1(input):
  x = 0
  y = 0
  dx = 0
  dy = 1
  wall = defaultdict(lambda: 0)
  painted = set()
  program = int_code(input, wall[f'{x}.{y}'])
  iterator = 0
  wall[f'{x}.{y}'] = next(program)
  painted.add(f'{x}.{y}')

  try:
    while True:
      if not iterator % 2:
        turn = next(program)
        dx, dy = change_direction(dx, dy, turn)
        x += dx
        y += dy
      else:
        wall[f'{x}.{y}'] = program.send(wall[f'{x}.{y}'])
        painted.add(f'{x}.{y}')
      iterator += 1
  except StopIteration:
    return len(painted)

def calculate2(input):
  x = 0
  y = 0
  dx = 0
  dy = 1
  wall = defaultdict(lambda: 0)
  wall[f'{x}.{y}'] = 1
  program = int_code(input, wall[f'{x}.{y}'])
  iterator = 0
  wall[f'{x}.{y}'] = next(program)

  try:
    while True:
      if not iterator % 2:
        turn = next(program)
        dx, dy = change_direction(dx, dy, turn)
        x += dx
        y += dy
      else:
        wall[f'{x}.{y}'] = program.send(wall[f'{x}.{y}'])
      iterator += 1
  except StopIteration:
    x_shift = abs(int(reduce(lambda a,b: a if int(a.split('.')[0]) < int(b.split('.')[0]) else b, wall.keys()).split('.')[0]))
    x_max = abs(int(reduce(lambda a,b: a if int(a.split('.')[0]) > int(b.split('.')[0]) else b, wall.keys()).split('.')[0]))
    y_shift = abs(int(reduce(lambda a,b: a if int(a.split('.')[1]) < int(b.split('.')[1]) else b, wall.keys()).split('.')[1]))
    y_max = abs(int(reduce(lambda a,b: a if int(a.split('.')[1]) > int(b.split('.')[1]) else b, wall.keys()).split('.')[1]))
    painting = np.array([0] * ((x_max + x_shift + 1) * (y_max + y_shift + 1))).reshape(y_max + y_shift + 1, x_max + x_shift + 1)

    for key, item in wall.items():
      x, y = [abs(int(i)) for i in key.split('.')]
      painting[y][x] = item
    return painting

print(calculate1(input), calculate2(input), sep='\n')