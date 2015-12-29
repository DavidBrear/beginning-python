NewClass = type('object', (), {})
NewClass.new_attr = 123
n = NewClass()
print 'n.new_attr is:', n.new_attr
print 'n is', n
