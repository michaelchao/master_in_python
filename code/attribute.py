class Me(object):
  pass

me = Me()

print('1 hasattr(me, "test"): {}'.format(hasattr(me, "test")))

if hasattr(me, "test"):
  print(getattr(me, "test"))

setattr(me, "test", "12")
print('2 hasattr(me, "test"): {}'.format(hasattr(me, "test")))
print('3 print(getattr(me, "test")): {}'.format(getattr(me, "test")))
print('4 me.test: {}'.format(me.test))
delattr(me, "test")
print('5 hasattr(me, "test"): {}'.format(hasattr(me, "test")))
print('6 isinstance(me, Me): {}'.format(isinstance(me, Me)))
print('7 issubclass(Me, object): {}'.format(issubclass(Me, object)))

# 1 hasattr(me, "test"): False
# 2 hasattr(me, "test"): True
# 3 print(getattr(me, "test")): 12
# 4 hasattr(me, "test"): False
# 5 isinstance(me, Me): True
# 6 issubclass(Me, object): True