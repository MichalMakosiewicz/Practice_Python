print(" --- --- ---" + '\n' +  "|   |   |   |" + '\n' + " --- --- ---" + '\n' + "|   |   |   |" + '\n' + ' --- --- ---' + '\n' + "|   |   |   |" + '\n' + " --- --- --- ")

def board():
    a = int(input("Wpisz rozmiar plansz a x a, a = "))

    print(" " + ("--- ") * a)

    for element in range(a):
        print("|" + (("   |") * a) + '\n' + " " + (("--- ") * a) )

board()