import random

lista = list([random.randint(0,1000) for r in range(9)])
lista.sort()

number = int(input("Wpisz liczbe: "))


def bin_look(number, lista):

    if number < int(lista[center]):
        lista = list([0, center])
    if number > int(lista[center]):
        lista = list([center, len(lista)])
    return lista

def center_list(lista):

    if len(lista) % 2 == 0:
        center = int((len(lista) + 1)/2)
        print(center)
        return center
    else:
        center = int(len(lista)/2)
        print(center)
        return center

test = True

while test == True:


    print(lista)
    print(lista[int(len(lista) / 2)])
    center = center_list(lista)

    if number == lista[center]:
        print("Numer jest w liscie!!!")
        test = False

    if len(lista) > 1:
        bin_look(number, lista)

    if len(lista) == 1 and list(number) != lista:
        print("numeru nie ma w liscie")
        test = False