num = int(input("wpisz numer:"))
check = int(input("Wpisz 2 numer:"))

if num % 4 ==0:
    print("Liczba podzielna przez 4 !!!")
elif num % 2 == 0:
    print("Liczba jest parzysta")

else:
    print("Liczba jest nie parzysta")

if num % check == 0:
    print("2 liczba jest dielnikiem 1")
else:
    print("2 liczba nie jest dzielnikiem 1")


