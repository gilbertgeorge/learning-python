import numpy as np


class TetrisBoard:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = np.full((height, width), '-')
        self.active_piece = None
        self.rotation = 0

    def __repr__(self):
        return str(f'width:{self.width}; height:{self.height}\n{self.board}')

    def print_board(self):
        print()
        for row_index in range(0, len(self.board)):
            printed_row = ''
            for column_index in range(0, len(self.board[row_index])):
                if self.active_piece:
                    base_index = int(f'{row_index}{column_index}', self.width)
                    if base_index in self.active_piece[self.rotation]:
                        printed_row += '0 '
                    else:
                        printed_row += f'{self.board[row_index][column_index]} '
                else:
                    printed_row += f'{self.board[row_index][column_index]} '
            print(f'{printed_row}')
        print()

    def add_piece(self, piece):
        self.active_piece = piece
        # print(self.active_piece)

    def move_piece(self, direction):
        if direction == 'left':
            for index in range(len(self.active_piece)):
                self.active_piece[index] = [x - 1 if x % self.width != 0 else x + self.width - 1
                                            for x in self.active_piece[index]]
            # print(self.active_piece, self.rotation)
        elif direction == 'right':
            for index in range(len(self.active_piece)):
                self.active_piece[index] = [x + 1 if (x + 1) % self.width != 0 else x - (self.width - 1)
                                            for x in self.active_piece[index]]
            # print(self.active_piece, self.rotation)
        elif direction == 'down':
            for index in range(len(self.active_piece)):
                self.active_piece[index] = [x + self.width for x in self.active_piece[index]]
            # print(self.active_piece, self.rotation)
        else:
            print('Invalid direction')
            return

    def rotate_piece(self, direction):
        if direction == 'clockwise':
            self.rotation = self.rotation - 1 if self.rotation > 0 else len(self.active_piece) - 1
            # print(self.active_piece, self.rotation)
        elif direction == 'counter-clockwise':
            self.rotation = self.rotation + 1 if self.rotation < len(self.active_piece) - 1 else 0
            # print(self.active_piece, self.rotation)


def tetris():
    new_piece_dictionary = {'O': [[4, 14, 15, 5]],
                            'I': [[4, 14, 24, 34], [3, 4, 5, 6]],
                            'S': [[5, 4, 14, 13], [4, 14, 15, 25]],
                            'Z': [[4, 5, 15, 16], [5, 15, 14, 24]],
                            'L': [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
                            'J': [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
                            'T': [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]}

    piece = input().upper()
    selected_piece = new_piece_dictionary[piece]
    board_dimensions = input().split()
    board = TetrisBoard(int(board_dimensions[0]), int(board_dimensions[1]))
    board.print_board()
    board.add_piece(selected_piece)
    board.print_board()
    while True:
        board.move_piece('down')
        command = input()
        if command == 'exit':
            break
        elif command == 'right' or command == 'left':
            board.move_piece(command)
        elif command == 'rotate':
            board.rotate_piece('counter-clockwise')
        board.print_board()


if __name__ == '__main__':
    tetris()

