name = input("Wpisz imię:")
age = input("Ile masz lat:")

age = int(age)
age2 = 2017 - age + 100
if age < 100:
    print(name + " w " + str(age2) + " roku bedziesz miał 100 lat")
else:
    print(name + "juz masz powyżej sto lat, Wszystkiego najlepszego!!!")