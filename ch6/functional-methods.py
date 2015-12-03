print map(str, range(10))

def func(x):
    return x.isalnum()

seq = ['foo', 'x41', '?!', '***']

print filter(func, seq)

d = [
    {'id': 1,
     'name': 'David Brear',
     'age': 30},
    {'id': 2,
     'name': 'Kelly Bryant',
     'age': 25},
    {'id': 2,
     'name': 'Kelly Bryant',
     'age': 25},
    {'id': 4,
     'name': 'Bill Gates',
     'age': 55},
    {'id': 1,
     'name': 'David Brear',
     'age': 30},
]

def uniq_users(users, primkey):
    seen = []
    def _uniq(user):
        if user['id'] not in seen:
            seen.append(user[primkey])
            return True
        return False
    return filter(_uniq, d)

for user in uniq_users(d, 'id'):
    print user['name']


# Reduce
numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]

print reduce(lambda x,y: x + y, numbers, 100)
