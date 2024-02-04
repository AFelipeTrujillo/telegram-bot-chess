import unittest
from unittest.mock import patch
from libs.chess import Game
from libs.bot import ChessBot
from libs.commands import GreetCommand, PlayCommand, UserMoveCommand

class TestChessBot(unittest.TestCase):
    def setUp(self):
        self.chess_game = Game()
        self.chess_bot = ChessBot("test_token", self.chess_game)

    def test_greet_command(self):
        greeting = GreetCommand().execute()
        self.assertEqual(greeting, "Hey! How are you? Click on /play to create a new game")

    def test_play_command(self):
        play_command = PlayCommand(self.chess_game)
        play_response = play_command.execute()
        self.assertIn("New chess game created", play_response)

    def test_user_move_command(self):
        user_move_command = UserMoveCommand(self.chess_game)
        user_move_command.move = "e2e4"
        with patch.object(self.chess_game, 'make_move', return_value="User move executed"):
            response = user_move_command.execute()
            self.assertIn("User move executed", response)

if __name__ == '__main__':
    unittest.main()
