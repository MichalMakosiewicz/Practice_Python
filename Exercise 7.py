import random

numlist = []
list_length = random.randint(5,15)

while len(numlist) < list_length:
    numlist.append(random.randint(1,1000))


even = [number for number in numlist if number % 2 == 0]

print(numlist)
print(even)