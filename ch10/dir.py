import copy
from pprint import pprint

pprint([n for n in dir(copy) if not n.startswith('_')])

pprint(copy.__all__)
