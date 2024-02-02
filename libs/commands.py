from libs.chess import Game

# Command Interface
class Command:
    def execute(self):
        pass

class GreetCommand(Command):
    def execute(self):
        return "Hey! How are you? click on /play to create a new game"
    
class PlayCommand(Command):

    def __init__(self, chess_game : Game) -> None:
        self.chess_game = chess_game
        super().__init__()

    def execute(self, move = None):
        if move:
            return self.chess_game.make_move(move)
        else:
            return self.chess_game.start_new_game()