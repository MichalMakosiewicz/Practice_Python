list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

list2 = []

a = int(input("Wpisz liczbę:"))

for element in list:
    if element < a:
       list2.append(element)


print(list2)
