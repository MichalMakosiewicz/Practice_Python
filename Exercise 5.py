import random

b = [random.randrange(0,1000) for r in range(20)]
c = [random.randrange(0,1000) for r in range(15)]

print(b)
print(c)

test = list(set(b).intersection(set(c)))

if test:
    print("The intersections are: ", test)
else:
    print("No intersection.")
