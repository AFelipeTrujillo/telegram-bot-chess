import telebot

from libs.chess import Game
from libs.commands import GreetCommand, PlayCommand, UserMoveCommand

class ChessBot:

    def __init__(self, token : str, chess_game : Game) -> None:
        self.bot = telebot.TeleBot(token, parse_mode='HTML')
        self.commands = {
            '/greeting': GreetCommand(),
            '/play' : PlayCommand(chess_game),
            '/user_move': UserMoveCommand(chess_game),
        }
        self.register_handlers()
    
    def register_handlers(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            
            command_parts = message.text.strip().split(" ")

            command = self.commands.get(command_parts[0])

            if command:
                if len(command_parts) > 1:
                    if isinstance(command, UserMoveCommand):
                        command.move = command_parts[1]
                    response = command.execute()
                else:
                    response = command.execute()
                self.bot.send_message(message.chat.id, response, parse_mode='HTML')
            else:
                self.bot.send_message(message.chat.id, "Unknown command")

    
    def run(self):
        self.bot.polling()


