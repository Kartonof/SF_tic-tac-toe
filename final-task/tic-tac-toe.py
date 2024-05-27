# карта
maps = [1,2,3,4,5,6,7,8,9]

# линии

winning_lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

# выводим картуъ
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])

    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])

    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])

# ход в ячейку
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# текущий результат
def get_result():
    win = ""

    for i in winning_lines:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "0" and maps[i[1]] == "0" and maps[i[2]] == "0":
            win = "0"
    return win

# сама игра
game_over = False
player1 = True

while game_over == False:
    print_maps()

    if player1 == True:
        symbol = "X"
        step = int(input("Ход первого игрока, укажи номер ячейки: "))
    else:
        symbol = "0"
        step = int(input("Ход второго игрока, укажи номер ячейки: "))
    
    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
    
    player1 = not(player1)

print_maps()
print("Победил", win)
