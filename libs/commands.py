import chess

import matplotlib
import matplotlib.pyplot as plt

from io import BytesIO
from telebot import TeleBot
from libs.chess import Game

matplotlib.use('Agg')

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

class UserMoveCommand(Command):
    def __init__(self, chess_game : Game, move):
        self.chess_game = chess_game
        self.move = move

    def execute(self):
        return self.chess_game.make_move(self.move)

class BotMoveCommand(Command):
    def __init__(self, chess_game : Game):
        self.chess_game = chess_game

    def execute(self):
        return self.chess_game.get_best_move()


class PositionImageCommand(Command):

    def __init__(self, chess_game : Game, bot : TeleBot):
        self.chess_game = chess_game
        self.bot = bot

    def execute(self): return self._generate_position_image()
    
    def _generate_position_image(self):
        board_svg = chess.svg.board(board=self.chess_game.board)
        print(board_svg)
        fig, ax = plt.subplots()
        ax.imshow([[]], cmap='gray')  # Adjust the background color as per your preferences
        ax.axis('off')
        fig.figimage(board_svg, resize=True)

        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)

        plt.close(fig)

        return img_buffer