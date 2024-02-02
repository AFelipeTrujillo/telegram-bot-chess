import telebot

from libs.chess import Game
from libs.commands import GreetCommand, PlayCommand

class ChessBot:

    def __init__(self, token : str, chess_game : Game) -> None:
        self.bot = telebot.TeleBot(token, parse_mode='HTML')
        self.commands = {
            '/greeting': GreetCommand(),
            '/play' : PlayCommand(chess_game)
        }
        self.register_handlers()
    
    def register_handlers(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            
            command_parts = message.text.strip().split(" ")

            command = self.commands.get(command_parts[0])

            if command:
                if len(command_parts) > 1:
                    response = command.execute(command_parts[1])
                else:
                    response = command.execute()
                self.bot.send_message(message.chat.id, response)
            else:
                self.bot.send_message(message.chat.id, "Unknown command")
    
    def run(self):
        self.bot.polling()


