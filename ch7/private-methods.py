class MyClass(object):

    def __methodname(cls):
        print 'calling the __methodname'

    def methodname(cls):
        print 'calling the methodname'


c = MyClass()

c.methodname()
c.__methodname()
