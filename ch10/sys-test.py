import sys
from pprint import pprint

methods = [n for n in dir(sys) if not n.startswith('_')]

# Useful methods:
#   argv
#   exit([arg])
#   modules
#   path
#   platform
#   stdin
#   stdout
#   stderr

pprint(methods)
