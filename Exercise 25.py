import random

a = 1
b = 100



def comp_choose():
    print(a)
    print(b)
    c = random.randint(a,b)
    print(c)
    return c

if __name__ == '__main__':
    gra = True
    while gra == True:

        comp_choose()
        hint = input("wiecej/mniej/zgadles :")

        if hint == "wiecej":
            a = int(c)


        if hint == "mniej":
            b = int(c)

        question = input("Dalej?(Tak):")
        if question == 'Tak':
            gra = True
        else:
            gra = False

