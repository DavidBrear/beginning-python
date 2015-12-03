x = 1

def change_global():
    global x
    x = 5

print 'x is', x
change_global()
print 'x is now', x