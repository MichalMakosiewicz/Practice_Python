with open('Ex23_1.txt', 'r') as ex1:
    lista1 = [line.strip() for line in ex1]

with open('Ex23_2.txt', 'r') as ex2:
    lista2 = [line.strip() for line in ex2]

porow = list(set(lista1).intersection(set(lista2)))

print(porow)