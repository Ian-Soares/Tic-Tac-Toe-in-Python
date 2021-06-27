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

def print_board_numbers():
    print(' 1 | 2 | 3 ')
    print('---|---|---')
    print(' 4 | 5 | 6 ')
    print('---|---|---')
    print(' 7 | 8 | 9 ')

def print_board():
    global board
    print(f' {board[0][0]} | {board[1][0]} | {board[2][0]} ')
    print('---|---|---')
    print(f' {board[3][0]} | {board[4][0]} | {board[5][0]} ')
    print('---|---|---')
    print(f' {board[6][0]} | {board[7][0]} | {board[8][0]} ')

def ask_move(letter):
    global board
    while True:
        try:
            move = input('Where will you play?: ').strip()
            print()
            if board[int(move)-1][0] == ' ':
                board[int(move)-1][0] = letter
                break
            elif int(move) > 9 or int(move) < 1: print(f'Sorry, but "{move}" is not an option.')
            else: print('This place may be occupied.')
        except ValueError:
            print('You need to enter some value!')
        except:
            print('Something went wrong, try again.')

def bot_move():
    global board
    PLAYERS = ['O','X']
    while True:
        for player in PLAYERS:
            # [0][0]
            if board[0][0] == board[1][0] and board[2][0] == ' ' and board[0][0] == player:
                board[2][0] = 'O'
                break

            elif board[0][0] == board[2][0] and board[1][0] == ' ' and board[0][0] == player:
                board[1][0] = 'O'
                break

            elif board[0][0] == board[4][0] and board[8][0] == ' ' and board[0][0] == player:
                board[8][0] = 'O'
                break
            
            elif board[0][0] == board[8][0] and board[4][0] == ' ' and board[0][0] == player:
                board[4][0] = 'O'
                break

            elif board[0][0] == board[3][0] and board[6][0] == ' ' and board[0][0] == player:
                board[6][0] = 'O'
                break

            elif board[0][0] == board[6][0] and board[3][0] == ' ' and board[0][0] == player:
                board[3][0] = 'O'
                break

            # [1][1]
            elif board[1][0] == board[2][0] and board[0][0] == ' ' and board[1][0] == player:
                board[0][0] = 'O'
                break

            elif board[1][0] == board[4][0] and board[7][0] == ' ' and board[1][0] == player:
                board[7][0] = 'O'
                break

            elif board[1][0] == board[7][0] and board[4][0] == ' ' and board[1][0] == player:
                board[4][0] = 'O'
                break

            # [2][0]
            elif board[2][0] == board[5][0] and board[8][0] == ' ' and board[2][0] == player:
                board[8][0] = 'O'
                break

            elif board[2][0] == board[8][0] and board[5][0] == ' ' and board[2][0] == player:
                board[5][0] = 'O'
                break

            elif board[2][0] == board[4][0] and board[6][0] == ' ' and board[2][0] == player:
                board[6][0] = 'O'
                break

            elif board[2][0] == board[6][0] and board[4][0] == ' ' and board[2][0] == player:
                board[4][0] = 'O'
                break

            # [3][0]
            elif board[3][0] == board[6][0] and board[0][0] == ' ' and board[3][0] == player:
                board[0][0] = 'O'
                break

            elif board[3][0] == board[4][0] and board[5][0] == ' ' and board[3][0] == player:
                board[5][0] = 'O'
                break

            elif board[3][0] == board[5][0] and board[4][0] == ' ' and board[3][0] == player:
                board[4][0] = 'O'
                break

            # [4][0]
            elif board[4][0] == board[8][0] and board[0][0] == ' ' and board[4][0] == player:
                board[0][0] = 'O'
                break

            elif board[4][0] == board[5][0] and board[3][0] == ' ' and board[4][0] == player:
                board[3][0] = 'O'
                break

            elif board[4][0] == board[7][0] and board[1][0] == ' ' and board[4][0] == player:
                board[1][0] = 'O'
                break

            elif board[4][0] == board[6][0] and board[2][0] == ' ' and board[4][0] == player:
                board[2][0] = 'O'
                break

            # [5][0]
            elif board[5][0] == board[8][0] and board[2][0] == ' ' and board[5][0] == player:
                board[2][0] = 'O'
                break

            # [6][0]
            elif board[6][0] == board[7][0] and board[8][0] == ' ' and board[6][0] == player:
                board[8][0] = 'O'
                break

            elif board[6][0] == board[8][0] and board[7][0] == ' ' and board[6][0] == player:
                board[7][0] = 'O'
                break

            # [7][0]
            elif board[7][0] == board[8][0] and board[6][0] == ' 'and board[7][0] == player:
                board[6][0] = 'O'
                break
            
        else:
            bot_move = randint(1,9)
            if board[bot_move-1][0] == ' ': 
                board[bot_move-1][0] = 'O'
                break
            else:
                continue
        break

def check_board_full():
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

def check_winner(player1,player2):
    global isThereWinner
    for i in 'X':
        if board[0][0] == i and board[1][0] == i and board[2][0] == i:
            isThereWinner = player1
        elif board[0][0] == i and board[3][0] == i and board[6][0] == i:
            isThereWinner = player1 
        elif board[0][0] == i and board[4][0] == i and board[8][0] == i:
            isThereWinner = player1 
        elif board[1][0] == i and board[4][0] == i and board[7][0] == i:
            isThereWinner = player1
        elif board[2][0] == i and board[5][0] == i and board[8][0] == i:
            isThereWinner = player1 
        elif board[2][0] == i and board[4][0] == i and board[6][0] == i:
            isThereWinner = player1 
        elif board[3][0] == i and board[4][0] == i and board[5][0] == i:
            isThereWinner = player1
        elif board[6][0] == i and board[7][0] == i and board[8][0] == i:
            isThereWinner = player1
    for i in 'O':
        if board[0][0] == i and board[1][0] == i and board[2][0] == i:
            isThereWinner = player2
        elif board[0][0] == i and board[3][0] == i and board[6][0] == i:
            isThereWinner = player2 
        elif board[0][0] == i and board[4][0] == i and board[8][0] == i:
            isThereWinner = player2
        elif board[1][0] == i and board[4][0] == i and board[7][0] == i:
            isThereWinner = player2
        elif board[2][0] == i and board[5][0] == i and board[8][0] == i:
            isThereWinner = player2
        elif board[2][0] == i and board[4][0] == i and board[6][0] == i:
            isThereWinner = player2
        elif board[3][0] == i and board[4][0] == i and board[5][0] == i:
            isThereWinner = player2
        elif board[6][0] == i and board[7][0] == i and board[8][0] == i:
            isThereWinner = player2

print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--- Welcome to the Tic Tac Toe in python ---
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

while True:
    try:
        choose_bot_or_two_players = input('Press [1] for 1v1, press [2] for a game against the bot: ').strip().replace('[','').replace(']','')
        if choose_bot_or_two_players == '1':
            game_type = '1v1'
            break
        elif choose_bot_or_two_players == '2':
            game_type = 'Against Bot'
            break
        else:
            print('There is not this option.')
    except:
        print('Please choose between those options (1 or 2).')

print()
print('--> You will be the X and need to inform where to play with numbers, just like this: ')
print()
print_board_numbers()
print('''
Good luck, here's the real board:
''')
print_board()

if game_type == 'Against Bot':

    while True:
        # PLAYER MOVE
        print()
        print(' > You play!')
        print()
        ask_move('X')
        print_board()
        check_winner('Player','Bot')
        check_board_full()
        if isBoardFull != 'N' or isThereWinner != 'N': break
        
        # BOT MOVE
        sleep(0.5)
        print()
        print(' > Bot\'s time!')
        print()
        sleep(0.5)
        bot_move()
        print_board()
        check_board_full()
        check_winner('Player','Bot')
        if isBoardFull != 'N' or isThereWinner != 'N': break

    if isThereWinner == 'Player': print('>>> Congratulations, you won!!! >>>')
    elif isThereWinner == 'Bot': print('<<< Well... that was good, but the bot won!!! <<<')
    else: print('>>> The game tied <<<')
    print('======================')
    print('   The game is over   ')
    print('======================')

elif game_type == '1v1':

    while True:
        # PLAYER 1 MOVE
        sleep(0.5)
        print()
        print(' > Player 1\'s time!')
        print()
        ask_move('X')
        print_board()
        check_winner('Player1','Player2')
        check_board_full()
        if isBoardFull != 'N' or isThereWinner != 'N': break
        
        # PLAYER 2 MOVE
        sleep(0.5)
        print()
        print(' > Player 2\'s time!')
        print()
        sleep(0.5)
        ask_move('O')
        print_board()
        check_board_full()
        check_winner('Player1','Player2')
        if isBoardFull != 'N' or isThereWinner != 'N': break

    if isThereWinner == 'Player1': print('>>> Congratulations, Player 1, you won it!!! <<<')
    elif isThereWinner == 'Player2': print('>>> Congratulations, Player 2, you won it!!! <<<')
    else: print('>>> The game tied <<<')
    print('======================')
    print('   The game is over   ')
    print('======================')
