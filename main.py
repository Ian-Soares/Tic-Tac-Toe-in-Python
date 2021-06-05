from random import randint
from time import sleep
global board
isBoardFull = 'N'
isThereWinner = 'N'

board = [
    [' '],[' '],[' '],
    [' '],[' '],[' '],
    [' '],[' '],[' ']
]

def printBoardNumbers():
    print(' 1 | 2 | 3 ')
    print('---|---|---')
    print(' 4 | 5 | 6 ')
    print('---|---|---')
    print(' 7 | 8 | 9 ')

def printBoard():
    global board
    print(f' {board[0][0]} | {board[1][0]} | {board[2][0]} ')
    print('---|---|---')
    print(f' {board[3][0]} | {board[4][0]} | {board[5][0]} ')
    print('---|---|---')
    print(f' {board[6][0]} | {board[7][0]} | {board[8][0]} ')

def askMove():
    global board
    while True:
        try:
            move = input('Where will you play?: ')
            if move == '1' and board[0][0] == ' ': 
                board[0][0] = 'X'
                break
            elif move == '2' and board[1][0] == ' ': 
                board[1][0] = 'X'
                break
            elif move == '3' and board[2][0] == ' ': 
                board[2][0] = 'X'
                break
            elif move == '4' and board[3][0] == ' ': 
                board[3][0] = 'X'
                break
            elif move == '5' and board[4][0] == ' ': 
                board[4][0] = 'X'
                break
            elif move == '6' and board[5][0] == ' ': 
                board[5][0] = 'X'
                break
            elif move == '7' and board[6][0] == ' ': 
                board[6][0] = 'X'
                break
            elif move == '8' and board[7][0] == ' ': 
                board[7][0] = 'X'
                break
            elif move == '9' and board[8][0] == ' ': 
                board[8][0] = 'X'
                break
            elif int(move) > 9 or int(move) < 1: print(f'Sorry, but "{move}" is not an option.')
            else: print('This place may be occupied.')
        except ValueError:
            print('You need to enter some value!')

def botMove():
    global board
    while True:
        bot_move = randint(1,9)
        if bot_move == 1 and board[0][0] == ' ': 
            board[0][0] = 'O'
            break
        elif bot_move == 2 and board[1][0] == ' ': 
            board[1][0] = 'O'
            break
        elif bot_move == 3 and board[2][0] == ' ': 
            board[2][0] = 'O'
            break
        elif bot_move == 4 and board[3][0] == ' ': 
            board[3][0] = 'O'
            break
        elif bot_move == 5 and board[4][0] == ' ': 
            board[4][0] = 'O'
            break
        elif bot_move == 6 and board[5][0] == ' ': 
            board[5][0] = 'O'
            break
        elif bot_move == 7 and board[6][0] == ' ': 
            board[6][0] = 'O'
            break
        elif bot_move == 8 and board[7][0] == ' ': 
            board[7][0] = 'O'
            break
        elif bot_move == 9 and board[8][0] == ' ': 
            board[8][0] = 'O'
            break
        else:
            continue

def checkBoardFull():
    global isBoardFull
    if board[0][0] != ' ' and \
        board[1][0] != ' ' and \
        board[2][0] != ' ' and \
        board[3][0] != ' ' and \
        board[4][0] != ' ' and \
        board[5][0] != ' ' and \
        board[6][0] != ' ' and \
        board[7][0] != ' ' and \
        board[8][0] != ' ': isBoardFull = 'Y'

def checkWinner():
    global isThereWinner
    '''
     0 | 1 | 2 
    ---|---|---
     3 | 4 | 5 
    ---|---|---
     6 | 7 | 8 
    '''
    for i in 'X':
        if board[0][0] == i and board[1][0] == i and board[2][0] == i:
            isThereWinner = 'Player'
        elif board[0][0] == i and board[3][0] == i and board[6][0] == i:
            isThereWinner = 'Player' 
        elif board[0][0] == i and board[4][0] == i and board[8][0] == i:
            isThereWinner = 'Player' 
        elif board[1][0] == i and board[4][0] == i and board[7][0] == i:
            isThereWinner = 'Player'
        elif board[2][0] == i and board[5][0] == i and board[8][0] == i:
            isThereWinner = 'Player' 
        elif board[2][0] == i and board[4][0] == i and board[6][0] == i:
            isThereWinner = 'Player' 
        elif board[3][0] == i and board[4][0] == i and board[5][0] == i:
            isThereWinner = 'Player'
        elif board[6][0] == i and board[7][0] == i and board[8][0] == i:
            isThereWinner = 'Player'
    for i in 'O':
        if board[0][0] == i and board[1][0] == i and board[2][0] == i:
            isThereWinner = 'Bot'
        elif board[0][0] == i and board[3][0] == i and board[6][0] == i:
            isThereWinner = 'Bot' 
        elif board[0][0] == i and board[4][0] == i and board[8][0] == i:
            isThereWinner = 'Bot' 
        elif board[1][0] == i and board[4][0] == i and board[7][0] == i:
            isThereWinner = 'Bot'
        elif board[2][0] == i and board[5][0] == i and board[8][0] == i:
            isThereWinner = 'Bot' 
        elif board[2][0] == i and board[4][0] == i and board[6][0] == i:
            isThereWinner = 'Bot' 
        elif board[3][0] == i and board[4][0] == i and board[5][0] == i:
            isThereWinner = 'Bot'
        elif board[6][0] == i and board[7][0] == i and board[8][0] == i:
            isThereWinner = 'Bot'

print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--- Welcome to the Tic Tac Toe in python ---
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will be the X and need to inform where to play with numbers, just like this:
''')
printBoardNumbers()
print('''
Good luck, here's the real board:
''')
printBoard()

while True:
    # PLAYER MOVE
    print()
    print('You play!')
    print()
    askMove()
    printBoard()
    checkWinner()
    checkBoardFull()
    if isBoardFull != 'N' or isThereWinner != 'N': break
    
    # BOT MOVE
    sleep(0.5)
    print()
    print('Bot\'s time!')
    print()
    sleep(0.5)
    botMove()
    printBoard()
    checkBoardFull()
    checkWinner()
    if isBoardFull != 'N' or isThereWinner != 'N': break

if isThereWinner == 'Player':
    print('>>> Congratulations, you won!!! >>>')
elif isThereWinner == 'Bot':
    print()
    print('<<< Well... that was good, but the bot won!!! <<<')
print('======================')
print('   The game is over   ')
print('======================')
