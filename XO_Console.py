import math
import time

# Initialize empty board
board = [" " for _ in range(9)]

def check_winner(board, player):
    """Check if a player has won the game"""
    # All possible winning combinations
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],  # Horizontal
        [0,3,6],[1,4,7],[2,5,8],  # Vertical
        [0,4,8],[2,4,6]           # Diagonal
    ]
    for s in win_states:
        if board[s[0]] == board[s[1]] == board[s[2]] == player:
            return True
    return False

def is_full(board):
    """Check if the board is completely filled"""
    return " " not in board

def alpha_beta(b, depth, maximizing, alpha, beta):
    """
    Alpha-Beta Pruning Algorithm:
    - AI (X) is maximizing: wants +1
    - Player (O) is minimizing: wants -1
    - Returns: +1 (AI wins), -1 (Player wins), 0 (draw)
    """
    # Base cases
    if check_winner(b, "X"):  # AI wins
        return 1
    if check_winner(b, "O"):  # Player wins
        return -1
    if is_full(b):            # Draw
        return 0

    if maximizing:
        best = -10000
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                val = alpha_beta(b, depth + 1, False, alpha, beta)
                b[i] = " "
                best = max(best, val)
                alpha = max(alpha, best)
                if alpha >= beta:  # Prune
                    break
        return best

    else:
        best = 10000
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                val = alpha_beta(b, depth + 1, True, alpha, beta)
                b[i] = " "
                best = min(best, val)
                beta = min(beta, best)
                if alpha >= beta:  # Prune
                    break
        return best

def best_move():
    """Find the best move for AI using alpha-beta pruning"""
    best_val = -10000
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            val = alpha_beta(board, 0, False, -10000, 10000)
            board[i] = " "
            if val > best_val:
                best_val = val
                move = i
    return move

def print_board():
    """Print the game board"""
    print("\n-------------")
    for i in range(0, 9, 3):
        print("|", board[i], "|", board[i+1], "|", board[i+2], "|")
    print("-------------\n")

# ═══════════════════════════════════════════
#           MAIN GAME LOOP
# ═══════════════════════════════════════════

print("=" * 40)
print("XO Game with Alpha-Beta Pruning")
print("=" * 40)
print("You are O, AI is X")
print("Board positions: 0-8")
print("\n 0 | 1 | 2")
print(" 3 | 4 | 5")
print(" 6 | 7 | 8\n")

while True:
    print_board()

    # Player's turn
    try:
        player_move = int(input("Enter position (0-8): "))
        if player_move > 8 or player_move < 0:
            print("Invalid! Please enter a number between 0-8")
            continue
        if board[player_move] != " ":
            print("Position already taken! Choose another.")
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue

    board[player_move] = "O"

    if check_winner(board, "O"):
        print_board()
        print("You Win! Incredible! (There might be a bug)")
        break

    if is_full(board):
        print_board()
        print("It's a Draw! Try again!")
        break

    # AI move
    print_board()
    print("AI is thinking...")
    time.sleep(1)
    move = best_move()
    board[move] = "X"

    if check_winner(board, "X"):
        print_board()
        print("AI Wins! Better luck next time!")
        break
