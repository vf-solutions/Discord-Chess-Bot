import chess
import chess.svg

class ChessGame:
    """One ChessGame for each match"""

    def __init__(self, challenger, member):
        self.board = chess.Board()
        self.moves = 0
        self.player = challenger
        self.players = (challenger, member)

    def make_move(self, move):
        try:
            uci = chess.Move.from_uci(move)
        except ValueError as e:
            return False
        if uci in self.board.legal_moves:
            self.board.push(uci)
            self.moves += 1
            self.board.apply_mirror()
            if self.board.is_game_over():
                return (True, self.board.result())
            self.player = self.players[self.moves % 2]
            return (True, None)
        else:
            return (False, None)

    def board_to_svg(self):
        return chess.svg.board(self.board, size=350)
