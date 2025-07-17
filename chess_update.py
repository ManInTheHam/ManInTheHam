import chess
import chess.svg
import cairosvg
from datetime import datetime

GAME_STATE_FILE = "game_state.txt"
README_FILE = "README.md"
BOARD_IMAGE_FILE = "board.png"

def load_game():
    import os
    if os.path.exists(GAME_STATE_FILE):
        with open(GAME_STATE_FILE, "r") as f:
            return chess.Board(f.read().strip())
    return chess.Board()

def save_game(board):
    with open(GAME_STATE_FILE, "w") as f:
        f.write(board.fen())

def render_board(board):
    svg = chess.svg.board(board=board)
    cairosvg.svg2png(bytestring=svg.encode('utf-8'), write_to=BOARD_IMAGE_FILE)

def update_readme():
    today = datetime.now().strftime("%Y-%m-%d")
    image_url = "https://raw.githubusercontent.com/ManInTheHam/ManInTheHam/main/board.png"

    with open(README_FILE, "w") as f:
        f.write(f"# 🐱‍👤 Soham Joshi\n\n")
        f.write(f"**`engineer (developer/shitposter)`**\n\n")
        f.write(f"I'm a developer, learning and building my digital world one step at a time...\n\n")
        f.write(f"### ♟️ Daily Chess Move\n\n")
        f.write(f"Today: {today}\n\n")
        f.write(f"<p align='center'>\n  <img src=\"{image_url}\" width=\"400\" />\n</p>\n")

if __name__ == "__main__":
    board = load_game()

    if not board.is_game_over():
        legal_moves = list(board.legal_moves)
        board.push(legal_moves[0])

    render_board(board)
    update_readme()
    save_game(board)
