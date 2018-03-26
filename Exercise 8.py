import random



def main():





    while True:

        #print("0")
        guess = get_player_guess()
        #print("1")
        komp = get_kom_choice()
        #print("2")
        get_moja_gra(guess, komp)
        #print("3")
        win()
        #print("4")
        victory = 0
        deafite = 0


        print("Wygrane: " + str(victory))
        print("Przegrane: " + str(deafite))

def get_player_guess():

    guess_guess = input("a = kamien, b = papier, c = nożyce:")
    return guess_guess

def get_kom_choice():

    list = ["a", "b", "c"]
    komp_komp = random.choice(list)
    print("Komputer wybrał " + komp_komp)
    return komp_komp

def get_moja_gra(guess,komp):

    if guess == "a" and komp == "c":
        win = '1'
        print("Wygrałeś")


    elif guess == "b" and komp == "a":
        win = '1'
        print("Wygrałeś")


    elif guess == "c" and komp == "b":
        win = '1'
        print("Wygrałeś")


    elif guess == komp:
        print("Jeszcze raz!")

    else:
        print("Przegrałeś")
        win = '2'



def win():

    if win == '1':
        victory = int(victory) + 1
    elif win == '2':
        deafite = int(deafite) + 1



main()




