a = int(input("Wpisz liczbe:"))

lista = list(range(1,a))
lista_2 = []
for element in lista:
    if a % element == 0:
        lista_2.append(element)

print(lista_2)