from game_board import board, position_index

player1 = 'X'
player2 = 'O'
restart_game = False
board = board
game_board = ','.join(board).replace(',', '')


def placement(command, player_no):
    global game_board
    if player_no % 2 == 0:
        update(command, player2)
        player2_position.append(int(command))
    else:
        update(command, player1)
        player1_position.append(int(command))

    game_board = ','.join(board).replace(',', '')
    print(game_board)


def check(player_no):
    if player_no % 2 == 0:
        player_position = player2_position
        message = 'Player 2 win'
    else:
        player_position = player1_position
        message = 'Player 1 win'

    if all(x in player_position for x in [1, 2, 3]):
        print(message)
        return True
    elif all(x in player_position for x in [4, 5, 6]):
        print(message)
        return True
    elif all(x in player_position for x in [7, 8, 9]):
        print(message)
        return True
    elif all(x in player_position for x in [1, 4, 7]):
        print(message)
        return True
    elif all(x in player_position for x in [2, 5, 8]):
        print(message)
        return True
    elif all(x in player_position for x in [3, 6, 9]):
        print(message)
        return True
    elif all(x in player_position for x in [1, 5, 9]):
        print(message)
        return True
    elif all(x in player_position for x in [3, 5, 7]):
        print(message)
        return True
    else:
        return False


def update(command, player):
    board[position_index[command]] = player
    return board


while not restart_game:
    print(game_board)
    player1_position = []
    player2_position = []
    for i in range(9):
        placement(input('Please select your placement'), i+1)
        print(player1_position, player2_position)
        if check(i+1):
            break

    print("It's a draw!!!")
    game = input('Do you want to play again? Y/N')
    if game.upper() == 'N':
        break
