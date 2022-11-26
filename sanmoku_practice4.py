import random

MARKS = {0:"X", 1:"O"}
GRID_NINE = 9
PLAYER0 = 0
PLAYER1 = 1

class Board:
    def __init__(self):
        self.state = [None] * 9

    def render(self):
        text = """
0|1|2
3|4|5
6|7|8"""
        for idx, x in enumerate(self.state):
            if x is not None:
                text = text.replace(str(idx), MARKS[x])
        print(text)

    def valid_moves(self):
        moves = []
        for idx, x in enumerate(self.state):
            if x is None:
                moves.append(idx)
        return moves

    def move(self, choice_move, player):
        self.state[choice_move] = player

    def unmove(self, choice_move):
        self.state[choice_move] = None

    def is_win(self, player):
        s = self.state
        if (
            s[0] == s[1] == s[2] == player or
            s[3] == s[4] == s[5] == player or
            s[6] == s[7] == s[8] == player or
            s[0] == s[3] == s[6] == player or
            s[1] == s[4] == s[7] == player or
            s[2] == s[5] == s[8] == player or
            s[0] == s[4] == s[8] == player or
            s[2] == s[4] == s[6] == player
        ):
            return True
        return False
    
    def is_end(self):
        if board.valid_moves() == []:
            return True
        return False

class HumanPlayer():
    def play(self, board, player):
        moves = board.valid_moves()
        choice_move = int(input(f"{moves}選択"))
        while choice_move not in moves:
            choice_move = int(input(f"{moves}選択"))
        board.move(choice_move, player)
        print(f"プレーヤー{MARKS[player]}指し手{choice_move}")
        board.render()

class RandomPlayer():
    def play(self, board, player):
        moves = board.valid_moves()
        choice_move = random.choice(moves)
        board.move(choice_move, player)
        print(f"プレーヤー{MARKS[player]}指し手{choice_move}")
        board.render()

class BetterPlayer():
    def play(self, board, player):
        moves = board.valid_moves()
        choice_move = random.choice(moves)
        for idx in moves:
            board.move(idx, player)
            if board.is_win(player):
                choice_move = idx
            board.unmove(idx)
        board.move(choice_move, player)
        print(f"プレーヤー{MARKS[player]}指し手{choice_move}")
        board.render()

class BestPlayer():
    def play(self, board, player):
        score, choice_move = self.minimax(board, player)
        board.move(choice_move, player)
        print(f"プレーヤー{MARKS[player]}指し手{choice_move}")
        print(score, choice_move)
        board.render()

    def minimax(self, board, player):
        moves = board.valid_moves()
        if player == 0:
            max_score = -20
            for idx in moves:
                board.move(idx, player)
                if board.is_win(player):
                    score = 10
                elif board.is_end():
                    score = 0
                elif board.is_win(PLAYER1):
                    score = -10
                else:
                    score, idx_r = self.minimax(board, PLAYER1)
                board.unmove(idx)

                if max_score < score:
                    max_score = score
                    choice_move = idx
            return max_score, choice_move
                
        if player == 1:
            min_score = 20
            for idx in moves:
                board.move(idx, player)
                if board.is_win(player):
                    score = -10
                elif board.is_end():
                    score = 0
                elif board.is_win(PLAYER0):
                    score = 10
                else:
                    score, idx_r = self.minimax(board, PLAYER0)
                board.unmove(idx)

                if min_score > score:
                    min_score = score
                    choice_move = idx
            return min_score, choice_move

board = Board()
board.render()

player0 = BestPlayer()
player1 = HumanPlayer()

while True:
    player0.play(board, PLAYER0)
    if board.is_win(PLAYER0):
        print(f"プレーヤーXの勝ち")
        break
    if board.is_end():
        print(f"引き分け")
        break
    player1.play(board, PLAYER1)
    if board.is_win(PLAYER1):
        print(f"プレーヤーOの勝ち")
        break
    if board.is_end():
        print(f"引き分け")
        break