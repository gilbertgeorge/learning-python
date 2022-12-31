import numpy as np


def print_board(piece=None):
    if piece is None:
        piece = []
    blank_board = np.array([['-', '-', '-', '-'],
                            ['-', '-', '-', '-'],
                            ['-', '-', '-', '-'],
                            ['-', '-', '-', '-']])

    for row_index in range(0, len(blank_board)):
        printed_row = ''
        for column_index in range(0, len(blank_board[row_index])):
            base_four = int(f'{row_index}{column_index}', 4)
            if base_four in piece:
                printed_row += '0 '
            else:
                printed_row += '- '
        print(f'{printed_row}')
    print()


def tetris():
    piece_dictionary = {'O': [[5, 6, 9, 10]],
                        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
                        'S': [[6, 5, 9, 8], [5, 9, 10, 14]],
                        'Z': [[4, 5, 9, 10], [2, 5, 6, 9]],
                        'L': [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]],
                        'J': [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]],
                        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]}
    piece = input().upper()
    selected_piece = piece_dictionary[piece]
    print_board()
    for rotation in range(0, 5):
        print_board(selected_piece[rotation % len(selected_piece)])


if __name__ == '__main__':
    tetris()
