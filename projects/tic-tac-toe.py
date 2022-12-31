def print_board_matrix(board_matrix):
    formatted_board = ''
    horizontal_boarder = '---------\n'
    formatted_board += horizontal_boarder
    for board_row in board_matrix:
        formatted_board += f'| {board_row[0]} {board_row[1]} {board_row[2]} |'
        formatted_board += '\n'
    formatted_board += horizontal_boarder
    print(formatted_board)


def generate_matrix(board):
    board_matrix = []
    board_row = []
    for board_index in range(len(board)):
        board_row.append(board[board_index])
        if len(board_row) % 3 == 0:
            board_matrix.append(board_row)
            board_row = []

    return board_matrix


def check_board_win(player, board):
    # check row win
    for board_row in board:
        if board_row[0] == player and board_row[1] == player and board_row[2] == player:
            return True

    # check column win
    for column_check in range(len(board[0])):
        matching_column = []
        [matching_column.append(row[column_index]) for row in board for column_index in range(len(row))
            if row[column_index] == player and column_index == column_check]
        if len(matching_column) == 3:
            return True

    # check diagonal win
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) \
            or (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True

    return False


def check_board_state(board, board_input):
    x_count = board_input.count('X')
    o_count = board_input.count('O')
    x_wins = check_board_win('X', board)
    o_wins = check_board_win('O', board)

    if (x_wins is True and o_wins is True) or abs(x_count - o_count) > 1:
        print('Impossible')
        return
    elif x_wins is True:
        print('X wins')
        return
    elif o_wins is True:
        print('O wins')
        return
    elif board_input.count('_') > 0:
        print('Game not finished')
        return
    else:
        print('Draw')
        return


def continue_game(board):
    x_wins = check_board_win('X', board)
    o_wins = check_board_win('O', board)
    if x_wins is True and o_wins is True:
        print('Impossible')
        return False
    elif x_wins is True:
        print('X wins')
        return False
    elif o_wins is True:
        print('O wins')
        return False
    elif len([item for row in board for item in row if item == ' ']) > 0:
        return True
    else:
        print('Draw')
        return False


def check_valid_move(player_move, board):
    string_coordinates = player_move.split()
    try:
        coordinates = [int(coordinate) for coordinate in string_coordinates]
    except ValueError:
        print('You should enter numbers!')
        return False
    for coordinate in coordinates:
        if 1 < coordinate > 3:
            print('Coordinates should be from 1 to 3!')
            return False
    if board[coordinates[0] - 1][coordinates[1] - 1] == 'X' or board[coordinates[0] - 1][coordinates[1] - 1] == 'O':
        print('This cell is occupied! Choose another one!')
        return False
    return True


def make_move(player, player_move, board):
    string_coordinates = player_move.split()
    coordinates = [int(coordinate) for coordinate in string_coordinates]
    board[coordinates[0] - 1][coordinates[1] - 1] = player
    return board


def tic_tac_toe():
    # board_input = input()
    players = ['X', 'O']
    current_player = 0
    board_input = ' ' * 9
    board = generate_matrix(board_input)
    print_board_matrix(board)

    while continue_game(board):
        while True:
            player_move = input()
            if check_valid_move(player_move, board):
                break

        board = make_move(players[current_player], player_move, board)
        print_board_matrix(board)
        current_player = (current_player + 1) % 2
    # check_board_state(board, board_input)


if __name__ == '__main__':
    tic_tac_toe()
