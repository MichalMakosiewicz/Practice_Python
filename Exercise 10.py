import random

b = [random.randrange(0,20) for r in range(10)]
c = [random.randrange(0,20) for r in range(10)]

print(b)
print(c)

test = list(set(b).intersection(set(c)))

print(test)