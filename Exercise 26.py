game = [[2,2,1],
        [1,1,2],
        [1,0,2]]

def check():
    if game[0][0] == game[1][0] == game[2][0]:
        print('gracz ' + str(game[0][0]) + ' wygrał')

    if game[0][1] == game[1][1] == game[2][1]:
        print('gracz ' + str(game[0][0]) + ' wygrał')

    if game[0][2] == game[1][2] == game[2][2]:
        print('gracz ' + str(game[0][0]) + ' wygrał')

    for element in game:
        if len(set(element)) == 1:
            print("gracz " + str(element[0]) + " wygrał")

    if game[0][0] == game[1][1] == game[2][2]:
        print('gracz ' + str(game[0][0]) + ' wygrał')

    if game[0][2] == game[1][1] == game[2][0]:
        print('gracz ' + str(game[2][0]) + ' wygrał')

check()