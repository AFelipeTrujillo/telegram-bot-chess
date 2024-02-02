# Chess Telegram Bot

Chess Telegram Bot is a simple Telegram bot that allows users to play chess and get game analysis using the Stockfish chess engine.

## Features

- Start a new chess game.
- Make moves during the game.
- Get suggestions for the best move using Stockfish.
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

### Usage
- Start a new game: /play
- Make a move: /user_move <move_in_uci_format>
- Get Bot move: /bot_move
- View the current board state: /board_state

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.