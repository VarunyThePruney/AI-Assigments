# games/tic_tac_toe.py

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            print("-" * 5)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def undo_move(self, position):
        self.board[position] = " "

    def winner(self, player):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True

        return False

    def is_draw(self):
        return " " not in self.board

    def game_over(self):
        return self.winner("X") or self.winner("O") or self.is_draw()