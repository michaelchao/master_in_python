
class MyContext(object):
  def __init__(self, string):
    self.string = string

  def __enter__(self):
    print('enter: {}'.format(self.string))

  def __exit__(self, exc_type, exc_val, exc_tb):
    print('exit: {}'.format(self.string))

with MyContext("michaelma") as c:
  print("process")

# enter: michaelma
# process
# exit: michaelma