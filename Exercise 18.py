import random


def compare(user_guess):
    cow = int(0)
    bull = int(0)
    for i in range(int(len((user_guess)))):
        if comp_guess[i] == user_guess[i]:
            bull += 1
        else:
            cow = len(set(user_guess).intersection(comp_guess))



    print('cows:' + str(cow))
    print('bools: ' + str(bull))
    return cow
    return bull



if __name__ =='__main__':
    gra = True
    comp_guess = list(str(random.randint(1000,9999)))
    print(comp_guess)
    guesses = 0



    while gra == True:
        user_guess = list(str(input("Wpisz 4 cyfry: ")))
        compare(user_guess)
        if user_guess == comp_guess:
            print("Wygrales")
            break