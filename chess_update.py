import chess
import chess.svg
from datetime import datetime
import base64
import os

GAME_STATE_FILE = "game_state.txt"
README_FILE = "README.md"
BOARD_IMAGE_FILE = "board.svg"

# Load the existing game or start a new one
def load_game():
    if os.path.exists(GAME_STATE_FILE):
        with open(GAME_STATE_FILE, "r") as f:
            return chess.Board(f.read().strip())
    return chess.Board()

# Save the current state
def save_game(board):
    with open(GAME_STATE_FILE, "w") as f:
        f.write(board.fen())

# Render SVG
def render_board(board):
    svg = chess.svg.board(board=board)
    with open(BOARD_IMAGE_FILE, "w") as f:
        f.write(svg)

# Update README
def update_readme():
    with open(BOARD_IMAGE_FILE, "r") as f:
        svg_content = f.read()
    today = datetime.now().strftime("%Y-%m-%d")
    
    with open(README_FILE, "w") as f:
        f.write(f"# ♟️ Daily Chess Move\n")
        f.write(f"Today: {today}\n\n")
        f.write(f"<div align='center'>\n{svg_content}\n</div>\n")

if __name__ == "__main__":
    board = load_game()

    # Simulate move (replace with actual move logic or user input)
    # Example: make a dummy move (e2e4) only if legal and game not over
    if not board.is_game_over():
        legal_moves = list(board.legal_moves)
        board.push(legal_moves[0])  # Take the first legal move

    render_board(board)
    update_readme()
    save_game(board)
