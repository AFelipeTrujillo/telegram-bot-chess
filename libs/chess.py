import chess
import chess.engine

class Game:

    def __init__(self) -> None:
        self.board = chess.Board()
    
    def start_new_game(self):
        self.board = chess.Board()
        return "New chess game created! You can start playing. Initial board state:\n" + self._format_board_state()
    
    def make_move(self, move):
        try:
            self.board.push(chess.Move.from_uci(move))
            return "Move successful! Updated board state:\n" + self._format_board_state()
        except ValueError:
            return "Invalid move. Please provide a valid UCI format move."
 
    def _format_board_state(self):
        return f"<pre>{str(self.board)}</pre>"

    def get_board_state(self):
        return str(self.board)