game = [[8,8,8],
        [8,8,8],
        [8,8,8]]




fun = True
while fun == True:


    print("gracz nr 1:")

    a = int(input("Który rząd wybierasz? (1/2/3): ")) - 1
    b = int(input("Którą komórkę wybierasz? (1/2/3): ")) - 1

    game[a][b] = 1

    for i in game:
        print(i)

    print("gracz nr 2:")

    c = int(input("Który rząd wybierasz? (1/2/3): ")) - 1
    d = int(input("Którą komórkę wybierasz? (1/2/3): ")) - 1

    game[c][d] = 2

    for i in game:
        print(i)