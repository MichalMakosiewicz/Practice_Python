
x = int(input("Ile liczb: "))

def pob_liczb(x):
    a = 0
    b = 1
    i = 1
    lista = []

    while i < x:
        a,b = b,b+a
        i += 1
        lista.append(a)
    return lista

print(pob_liczb(x))