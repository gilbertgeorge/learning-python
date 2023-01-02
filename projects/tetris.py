import numpy as np


class TetrisBoard:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = np.full((height, width), '-')
        self.active_piece = None
        self.rotation = 0
        self.piece_landed = False
        self.game_over = False
        self.floor = [self.width * self.height + x for x in range(0, self.width)]

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
            print(f'{printed_row.strip()}')
        print()
        # print(self.active_piece, self.rotation, self.floor)

    def add_piece(self, piece):
        self.active_piece = piece
        self.rotation = 0
        self.piece_landed = False

    def apply_piece(self, piece):
        for pixel in piece:
            self.board[int(pixel / self.width)][pixel % self.width] = '0'
        self.active_piece = None

    def check_for_game_over(self):
        if any(int(element / self.width) == 0 for element in self.floor):
            self.game_over = True

    def clear_lines(self):
        for row_index in range(0, len(self.board)):
            if all(element == '0' for element in self.board[row_index]):
                self.board = np.delete(self.board, row_index, 0)
                self.board = np.insert(self.board, 0, '-', 0)
                row_to_remove = [(row_index * self.width + x) for x in range(self.width)]
                self.floor = [elem for elem in self.floor if elem not in row_to_remove]
                self.floor = [elem for elem in self.floor if elem > self.width * self.height] +\
                             [elem + self.width for elem in self.floor if elem < self.width * row_index]

    def move_piece(self, direction):
        if direction == 'left' and not self.piece_landed:
            if all(element % self.width != 0 for element in self.active_piece[self.rotation]):
                for index in range(len(self.active_piece)):
                    self.active_piece[index] = [x - 1 for x in self.active_piece[index]]
        elif direction == 'right' and not self.piece_landed:
            if all((element + 1) % self.width != 0 for element in self.active_piece[self.rotation]):
                for index in range(len(self.active_piece)):
                    self.active_piece[index] = [x + 1 for x in self.active_piece[index]]
        elif direction == 'down' and not self.piece_landed:
            if any((element + self.width) in self.floor for element in self.active_piece[self.rotation]):
                # print(f'piece landed {self.active_piece}')
                self.floor.extend(self.active_piece[self.rotation])
                self.apply_piece(self.active_piece[self.rotation])
                self.piece_landed = True
                self.check_for_game_over()
            else:
                for index in range(len(self.active_piece)):
                    self.active_piece[index] = [x + self.width for x in self.active_piece[index]]

    def rotate_piece(self, direction):
        if direction == 'clockwise' and not self.piece_landed:
            self.rotation = self.rotation - 1 if self.rotation > 0 else len(self.active_piece) - 1
        elif direction == 'counter-clockwise' and not self.piece_landed:
            self.rotation = self.rotation + 1 if self.rotation < len(self.active_piece) - 1 else 0


def tetris():
    new_piece_dictionary = {'O': [[4, 14, 15, 5]],
                            'I': [[4, 14, 24, 34], [3, 4, 5, 6]],
                            'S': [[5, 4, 14, 13], [4, 14, 15, 25]],
                            'Z': [[4, 5, 15, 16], [5, 15, 14, 24]],
                            'L': [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
                            'J': [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
                            'T': [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]}

    board_dimensions = input().split()
    board = TetrisBoard(int(board_dimensions[0]), int(board_dimensions[1]))
    board.print_board()

    while board.game_over is False:
        command = input()
        if command == 'exit':
            break
        elif command == 'piece':
            piece = input().upper()
            selected_piece = list(new_piece_dictionary[piece])
            board.add_piece(selected_piece)
        elif command == 'right' or command == 'left':
            board.move_piece(command)
            board.move_piece('down')
        elif command == 'rotate':
            board.rotate_piece('counter-clockwise')
            board.move_piece('down')
        elif command == 'down':
            board.move_piece(command)
        elif command == 'break':
            board.clear_lines()
        board.print_board()
    print('Game Over!')


if __name__ == '__main__':
    tetris()

