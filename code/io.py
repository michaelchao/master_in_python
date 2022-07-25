import sys

def stdoutToFile(filename, function, args):
  '''
    stdoutToFile('m.txt', help, "modules")
  '''
  oldStdout = sys.stdout
  f = open(filename, 'w')
  sys.stdout = f
  function(args)
  sys.stdout.flush()
  sys.stdout = oldStdout
  f.close()

