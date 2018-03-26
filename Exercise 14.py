import random

def make_list():
    lista = []

    for i in range(10):
        lista.append(random.randint(1,10))

    return lista


def bez_powt():
    a = make_list()
    b = set(a)
    print(b)

print(make_list())
print(bez_powt())