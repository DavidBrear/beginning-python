import fileinput

methods = [n for n in dir(fileinput) if not n.startswith('_')]

# Useful methods:
#   input([files[, inplace[, backup]]])
#   filename
#   lineno
#   filelineno
#   isfirstline
#   isstdin
#   nextfile
#   close

print(methods)
