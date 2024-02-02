import os

from libs.chess import Game
from libs.bot import ChessBot

from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TELEGRAM_TOKEN")

chess_game = Game()

chess_bot = ChessBot(token, chess_game)

chess_bot.run()