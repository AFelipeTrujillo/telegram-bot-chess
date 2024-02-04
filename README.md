# Telegram Chess Bot

This is a simple Telegram bot for playing chess. The bot allows users to start new games, make moves, and receive responses from the bot. It uses the **python-chess** library for chess-related functionalities.

## Features

- Start a new chess game.
- Make moves during the game.
- Get bot move using **Stockfish**.
- View the current state of the chess board.

## Getting Started

### Prerequisites

- Python 3.x
- Stockfish Chess Engine (download from [Stockfish Website](https://stockfishchess.org/download/))

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AFelipeTrujillo/chess-telegram-bot.git
   cd chess-telegram-bot

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt

3. Download and install Stockfish from Stockfish Website.

4. Update the stockfish_path variable in the ChessGame class within the code to the path of your Stockfish executable.

5. Run the bot:

    ```bash
    python main.py

## Project Structure

- **libs**: Contains modules for the chess bot functionality.
  - `bot.py`: Defines the ChessBot class.
  - `chess.py`: Contains the Game class and related chess functionalities.
  - `commands.py`: Defines various command classes for the bot.

- **tests**: Contains unit tests for the bot functionalities.

- **.env**: File for storing environment variables, including the Telegram API token.

- **main.py**: Entry point for running the bot.

## Usage
- Start a new game: /play
- Make a move: /user_move <move_in_uci_format>
- View the current board state: /board_state

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.