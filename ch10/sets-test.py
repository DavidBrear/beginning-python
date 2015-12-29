print(set(range(10)))
print(set([0,1,2,3,0,1,2,3,4,5]))

print(set(['fee', 'fie', 'foe']))

a = set([1,2,3])
b = set([2,3,4])
print 'a:', a
print 'b:', b

# Union
print 'Union:'
print 'a.union(b):', a.union(b)
print 'a | b:', a | b

# Subset
c = a & b
print 'c = a & b:', c
print 'c.issubset(a):', c.issubset(a)
print 'c <= a:', c <= a

# Superset
print 'c.issuperset(a):', c.issuperset(a)
print 'c >= a:', c >= a

# Intersection
print 'a.intersection(b):', a.intersection(b)
print 'a & b:', a & b

print 'a.difference(b):', a.difference(b)
print 'a - b:', a - b

print 'a.symmetric_difference(b):', a.symmetric_difference(b)
print 'a ^ b:', a ^ b

print 'a.copy():', a.copy()
print 'a.copy() is a:', a.copy() is a
