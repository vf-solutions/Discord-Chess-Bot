import chess
import chess.svg

class ChessGame:
    """One ChessGame for each match"""

    def __init__(self, challenger, member):
        self.board = chess.Board()
        self.moves = 0
        self.player = challenger
        self.players = (challenger, member)
        self.last_move = None

    def make_move(self, move):
        try:
            uci = chess.Move.from_uci(move)
            self.last_move = uci
        except ValueError as e:
            return (False, None)
        if uci in self.board.legal_moves:
            self.board.push(uci)
            self.moves += 1
            if self.board.is_game_over():
                return (True, self.board.result())
            self.player = self.players[self.moves % 2]
            return (True, None)
        else:
            return (False, None)

    def board_to_svg(self):
        if self.board.is_check():
            bk = self.board.king(chess.BLACK)
            wk = self.board.king(chess.WHITE)
            if self.board.is_attacked_by(chess.WHITE, bk):
                check = bk
            else:
                check = wk
        else:
            check = None
        return chess.svg.board(self.board, size=350, check=check, lastmove=self.last_move, orientation=(self.player==self.players[0]))
