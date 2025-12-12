import tkinter as tk
import random
import math

# -------------------------
# Game / AI logic
# -------------------------
def check_win_for(b, player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b_,c in wins:
        if b[a] == b[b_] == b[c] == player:
            return True
    return False

def minimax(b, depth, is_max):
    if check_win_for(b, "O"):
        return 1
    if check_win_for(b, "X"):
        return -1
    if "" not in b:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == "":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = ""
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == "":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = ""
                best = min(best, score)
        return best

def best_move_full(board_state):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board_state[i] == "":
            board_state[i] = "O"
            move_val = minimax(board_state, 0, False)
            board_state[i] = ""
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def medium_move(board_state):
    # 30% random + 70% smart
    if random.random() < 0.3:
        choices = [i for i in range(9) if board_state[i] == ""]
        return random.choice(choices)
    return best_move_full(board_state)

def easy_move(board_state):
    choices = [i for i in range(9) if board_state[i] == ""]
    return random.choice(choices)

# -------------------------
# Tkinter GUI
# -------------------------
root = tk.Tk()
root.title("Tic Tac Toe - AI Challenge")
root.geometry("700x600")
root.resizable(False, False)
root.configure(bg='#1a1a2e')

# Color scheme
BG_COLOR = '#1a1a2e'
BG_SECONDARY = '#16213e'
ACCENT_COLOR = '#0f3460'
TEXT_COLOR = '#eee'
BUTTON_COLOR = '#e94560'
BUTTON_HOVER = '#ff6b81'
X_COLOR = '#00d9ff'
O_COLOR = '#ff6b81'

# Fonts
FONT_TITLE = ("Helvetica", 28, "bold")
FONT_SUBTITLE = ("Helvetica", 14)
FONT_NORMAL = ("Helvetica", 12)
FONT_BUTTON = ("Helvetica", 11, "bold")
FONT_BOARD = ("Helvetica", 32, "bold")

# global state
difficulty = "Easy"   # default
board = [""] * 9
buttons = []

# -------------------------
# Frame helpers (screens)
# -------------------------
main_menu_frame = tk.Frame(root, bg=BG_COLOR)
game_frame = tk.Frame(root, bg=BG_COLOR)

def hide_all_frames():
    for f in (main_menu_frame, game_frame):
        f.pack_forget()

# -------------------------
# Game Menu and Game Screen
# -------------------------
def show_game_menu():
    hide_all_frames()
    menu = tk.Toplevel(root)
    menu.title("Choose Difficulty")
    menu.geometry("400x450")
    menu.configure(bg=BG_COLOR)
    menu.resizable(False, False)
    
    tk.Label(menu, text="🎯 Select Difficulty", font=FONT_TITLE, 
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=30)
    
    def create_diff_button(text, level, emoji):
        btn = tk.Button(menu, text=f"{emoji} {text}", font=FONT_BUTTON,
                       bg=ACCENT_COLOR, fg='white',
                       activebackground=BUTTON_COLOR, activeforeground='white',
                       width=18, height=2, bd=0, cursor='hand2',
                       command=lambda: start_game(level, menu))
        btn.pack(pady=12)
        btn.bind('<Enter>', lambda e: btn.config(bg=BUTTON_COLOR))
        btn.bind('<Leave>', lambda e: btn.config(bg=ACCENT_COLOR))
    
    create_diff_button("EASY", "Easy", "😊")
    create_diff_button("MEDIUM", "Medium", "🤔")
    create_diff_button("HARD", "Hard", "😈")
    
    cancel_btn = tk.Button(menu, text="← BACK", font=FONT_BUTTON,
                          bg=BG_SECONDARY, fg=TEXT_COLOR,
                          activebackground=ACCENT_COLOR, activeforeground='white',
                          width=18, height=2, bd=0, cursor='hand2',
                          command=menu.destroy)
    cancel_btn.pack(pady=20)
    cancel_btn.bind('<Enter>', lambda e: cancel_btn.config(bg=ACCENT_COLOR))
    cancel_btn.bind('<Leave>', lambda e: cancel_btn.config(bg=BG_SECONDARY))

def start_game(level, menu_window=None):
    global difficulty
    difficulty = level
    if menu_window:
        menu_window.destroy()
    hide_all_frames()
    setup_game_screen()
    game_frame.pack(expand=True, fill='both')

# Game screen builder
def setup_game_screen():
    for w in game_frame.winfo_children():
        w.destroy()

    # Header
    header_frame = tk.Frame(game_frame, bg=BG_COLOR)
    header_frame.pack(pady=(20,10))
    
    difficulty_emoji = {"Easy": "😊", "Medium": "🤔", "Hard": "😈"}
    tk.Label(header_frame, text=f"You: ❌  vs  AI: ⭕", 
             font=FONT_SUBTITLE, bg=BG_COLOR, fg=TEXT_COLOR).pack()
    tk.Label(header_frame, text=f"{difficulty_emoji.get(difficulty, '')} {difficulty} Mode", 
             font=FONT_NORMAL, bg=BG_COLOR, fg=ACCENT_COLOR).pack()
    
    # Board frame with border
    board_container = tk.Frame(game_frame, bg=ACCENT_COLOR, padx=3, pady=3)
    board_container.pack(pady=20)
    
    board_frame = tk.Frame(board_container, bg=BG_SECONDARY)
    board_frame.pack()

    global board, buttons
    board = [""] * 9
    buttons = []

    def click_btn(i):
        if board[i] == "":
            board[i] = "X"
            buttons[i].config(text="X", fg=X_COLOR, state=tk.DISABLED, 
                            disabledforeground=X_COLOR)
            if check_win_for(board, "X"):
                root.after(300, lambda: show_winner("You Win! 🎉", X_COLOR))
                return
            if "" not in board:
                root.after(300, lambda: show_winner("It's a Draw! 🤝", TEXT_COLOR))
                return
            root.after(300, ai_turn)

    for i in range(9):
        btn = tk.Button(board_frame, text="", font=FONT_BOARD, width=4, height=2,
                       bg=BG_SECONDARY, fg=TEXT_COLOR,
                       activebackground=ACCENT_COLOR, activeforeground=TEXT_COLOR,
                       bd=0, cursor='hand2',
                       command=lambda i=i: click_btn(i))
        btn.grid(row=i//3, column=i%3, padx=2, pady=2)
        buttons.append(btn)

    # Control buttons
    control_frame = tk.Frame(game_frame, bg=BG_COLOR)
    control_frame.pack(pady=20)
    
    def create_control_btn(text, command, col):
        btn = tk.Button(control_frame, text=text, font=FONT_BUTTON,
                       bg=ACCENT_COLOR, fg='white',
                       activebackground=BUTTON_COLOR, activeforeground='white',
                       width=15, height=2, bd=0, cursor='hand2',
                       command=command)
        btn.grid(row=0, column=col, padx=10)
        btn.bind('<Enter>', lambda e: btn.config(bg=BUTTON_COLOR))
        btn.bind('<Leave>', lambda e: btn.config(bg=ACCENT_COLOR))
    
    create_control_btn("🔄 RESET", reset_board_ui, 0)
    create_control_btn("🏠 MENU", show_main_menu, 1)

def ai_turn():
    global board, buttons
    if "" not in board:
        return
    if difficulty == "Easy":
        move = easy_move(board)
    elif difficulty == "Medium":
        move = medium_move(board)
    else:
        move = best_move_full(board)
    board[move] = "O"
    buttons[move].config(text="O", fg=O_COLOR, state=tk.DISABLED,
                        disabledforeground=O_COLOR)
    if check_win_for(board, "O"):
        root.after(300, lambda: show_winner("AI Wins! 🤖", O_COLOR))
        return
    if "" not in board:
        root.after(300, lambda: show_winner("It's a Draw! 🤝", TEXT_COLOR))
        return

def show_winner(message, color):
    win = tk.Toplevel(root)
    win.title("Game Over")
    win.geometry("350x250")
    win.configure(bg=BG_COLOR)
    win.resizable(False, False)
    
    tk.Label(win, text=message, font=FONT_TITLE,
             bg=BG_COLOR, fg=color).pack(pady=40)
    
    def create_result_btn(text, command):
        btn = tk.Button(win, text=text, font=FONT_BUTTON,
                       bg=BUTTON_COLOR, fg='white',
                       activebackground=BUTTON_HOVER, activeforeground='white',
                       width=15, height=2, bd=0, cursor='hand2',
                       command=command)
        btn.pack(pady=8)
        btn.bind('<Enter>', lambda e: btn.config(bg=BUTTON_HOVER))
        btn.bind('<Leave>', lambda e: btn.config(bg=BUTTON_COLOR))
    
    create_result_btn("🔄 PLAY AGAIN", lambda: (win.destroy(), reset_board_ui()))
    create_result_btn("🏠 MAIN MENU", lambda: (win.destroy(), show_main_menu()))

def reset_board_ui():
    global board, buttons
    board = [""] * 9
    for b in buttons:
        b.config(text="", state=tk.NORMAL, bg=BG_SECONDARY)

def create_menu_button(parent, text, command):
    btn = tk.Button(parent, text=text, font=FONT_BUTTON, 
                   bg=BUTTON_COLOR, fg='white', 
                   activebackground=BUTTON_HOVER, activeforeground='white',
                   width=20, height=2, bd=0, cursor='hand2',
                   command=command)
    btn.pack(pady=10)
    btn.bind('<Enter>', lambda e: btn.config(bg=BUTTON_HOVER))
    btn.bind('<Leave>', lambda e: btn.config(bg=BUTTON_COLOR))

def show_main_menu():
    hide_all_frames()
    # Clear and rebuild the menu
    for widget in main_menu_frame.winfo_children():
        widget.destroy()
    
    # Title
    tk.Label(main_menu_frame, text="⭕ TIC TAC TOE ❌", font=FONT_TITLE, 
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(50,10))

    tk.Label(main_menu_frame, text="Challenge the AI", font=FONT_SUBTITLE, 
             bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=(0,40))

    create_menu_button(main_menu_frame, "🎮 PLAY GAME", show_game_menu)
    create_menu_button(main_menu_frame, "🚪 EXIT", root.quit)
    main_menu_frame.pack(expand=True, fill='both')



# -------------------------
# Start
# -------------------------
show_main_menu()
root.mainloop()
