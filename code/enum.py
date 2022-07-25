
# way1
class Direction:
  Up = 0
  Down = 1
  Left = 2
  Right = 3

print(Direction.Left)

# way2

dirUp, dirDown, dirLeft, dirDown = range(4)
print(dirLeft)

# way3
import collections
dircoll = collections.namedtuple('direction', ('Up', 'Down', 'Left', 'Right'))
directions = dircoll(0, 1, 2, 3)
print(directions.Left)

# way4
Dir = {'Up': 0, 'Down': 1, 'Left': 2, 'Right':3}
print(Dir['Left'])

# way5
def enum(args, start=0):
  class Enum(object):
    __slot__ = args.split()
    def __init__(self):
      for i, key in enumerate(Enum.__slot__, start):
        setattr(self, key, i)
  return Enum()

e_dir = enum('Up Down Left Right')
print(e_dir.Left)