import os
def start_board():
    os.system("cls")
    print('  1  |  2  |  3  ')
    print('-----+-----+-----')
    print('  4  |  5  |  6  ')
    print('-----+-----+-----')
    print('  7  |  8  |  9  ')

def win():
    flag = 0
    for i in board.values():
        if i == ' ':
            flag = 1
            break
    if board[1] == board[2] == board[3] != ' ':
        if board[1] == 'X':
            print('Player 1 won')
        elif board[1] == 'O':
            print('Player 2 won')
        return True
    elif board[4] == board[5] == board[6] != ' ':
        if board[4] == 'X':
            print('Player 1 won')
        elif board[4] == 'O':
            print('Player 2 won')
        return True
    elif board[7] == board[8] == board[9] != ' ':
        if board[7] == 'X':
            print('Player 1 won')
        elif board[7] == 'O':
            print('Player 2 won')
        return True
    elif board[1] == board[4] == board[7] != ' ':
        if board[1] == 'X':
            print('Player 1 won')
        elif board[1] == 'O':
            print('Player 2 won')
        return True
    elif board[2] == board[5] == board[8] != ' ':
        if board[2] == 'X':
            print('Player 1 won')
        elif board[2] == 'O':
            print('Player 2 won')
        return True
    elif board[3] == board[6] == board[9] != ' ':
        if board[3] == 'X':
            print('Player 1 won')
        elif board[3] == 'O':
            print('Player 2 won')
        return True
    elif board[1] == board[5] == board[9] != ' ':
        if board[1] == 'X':
            print('Player 1 won')
        elif board[1] == 'O':
            print('Player 2 won')
        return True
    elif board[3] == board[5] == board[7] != ' ':
        if board[3] == 'X':
            print('Player 1 won')
        elif board[3] == 'O':
            print('Player 2 won')
        return True
    elif flag == 0:
        print('Its a tie')
        return True
    else:
        return False

def enter_move():
    while True:
        try:
            i = int(input())
        except ValueError:
            print('Your input is not valid. Enter another move')
            continue
        if i not in range(1,10):
            print('Wrong Input\nEnter your position again')
        elif board[i] != ' ':
            print('Move already used. Enter another move')
        else:
            print('Move Registered')
            break
    return i

def current_board():
    print('  '+board[1]+'  |  '+board[2]+'  |  '+board[3]+'  ')
    print('-----+-----+-----')
    print('  '+board[4]+'  |  '+board[5]+'  |  '+board[6]+'  ')
    print('-----+-----+-----')
    print('  '+board[7]+'  |  '+board[8]+'  |  '+board[9]+'  ')


play = 'Y'

print('Do you want to play this game\n Press N for No and anything else for Yes:')
play = input()

while True:
    if play == 'N' or play == 'n':
        break
    start_board()
    chance = 1
    won = False
    board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    while won is not True:
        print('Enter the move of player',chance)
        move = enter_move()
        if chance == 1:
            board[move] = 'X'
        elif chance == 2:
            board[move] = 'O'
        current_board()
        won = win()
        if chance == 1:
            chance += 1
        elif chance == 2:
            chance -= 1

    print('Do you wanna continue. \nPress N for No and anything else for Yes')
    play = input()
