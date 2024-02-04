import chess
import chess.engine

from chess.engine import SimpleEngine

class Game:

    def __init__(self) -> None:
        self.board = chess.Board()
        self.stockfish : SimpleEngine = SimpleEngine.popen_uci('/usr/local/bin/stockfish')
        self.current_player = chess.WHITE
    
    def start_new_game(self):
        self.board = chess.Board()
        return "New chess game created! You can start playing. Initial board state:\n" + self._format_board_state()
    
    def make_move(self, move):
        try:
            self.board.push(chess.Move.from_uci(move))
            self.current_player = not self.current_player
            return f"Move successful! Updated board state: <b>{move}</b>\n{self._format_board_state()}"
        except ValueError:
            return "Invalid move. Please provide a valid UCI format move."
 
    def get_best_move(self):
        if self.current_player == chess.BLACK:
            result = self.stockfish.play(self.board, chess.engine.Limit(time=2.0))
            self.board.push(result.move)
            self.current_player = not self.current_player
            return f"Move successful! Updated board state: <b>{result.move.uci()}</b>\n" + self._format_board_state() 
    
    def _format_board_state(self) -> str:
        return f"<pre>{str(self.board)}</pre>"

    def get_board_state(self) -> str:
        return str(self.board)