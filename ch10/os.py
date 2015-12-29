import os

methods = [n for n in dir(os) if not n.startswith('_')]

# Useful methods:
#   environ
#   system(command)
#   sep
#   pathsep
#   linesep
#   urandom(n)

print(methods)
