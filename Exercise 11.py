def czy_pierwsza():
    x = int(input("Twój numer: \n"))
    for i in range(2, round(x/2)+2):
        if x % i == 0:
            print("Masz liczbe nie pierwszą")
            break
        else:
            print("Liczba pierwsza")
            break

czy_pierwsza()