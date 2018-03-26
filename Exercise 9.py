import random

a = random.randint(1,10)

b = 0

c = 1

while b != a:

    print("Proba: " + str(c))

    b = input("Zgadni liczbe 1 - 9: ")

    if b == "exit":
        print("Dzieki za gre")
        break

    b = int(b)

    if b > a:
        print("Za duzo")
        c += 1

    elif b < a:
        print("Za malo")
        c += 1

    else:
        print("Brawo")