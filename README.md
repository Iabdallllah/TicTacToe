# 🎮 Tic Tac Toe - AI Challenge

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**A modern, interactive Tic Tac Toe game with intelligent AI opponent**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works) • [Screenshots](#-screenshots)

</div>

---

## ✨ Features

### 🎨 **Modern UI/UX**
- Dark-themed interface with stunning color palette
- Smooth hover effects and animations
- Intuitive button designs with emoji icons
- Responsive and polished layout

### 🤖 **Intelligent AI**
- **Easy Mode**: Random moves for beginners 😊
- **Medium Mode**: Mix of random and strategic moves 🤔
- **Hard Mode**: Unbeatable AI using Minimax algorithm 😈

### 🎯 **Gameplay Features**
- Single-player vs AI
- Real-time move validation
- Win/Draw detection with custom dialogs
- Board reset functionality
- Easy navigation between menus

---

## 📋 Requirements

- **Python 3.7 or higher**
- **Tkinter** (usually comes pre-installed with Python)

---

## 🚀 Installation

### Option 1: Clone the Repository
```bash
git clone https://github.com/yourusername/TicTacToe-AI.git
cd TicTacToe-AI
```

### Option 2: Download ZIP
Download the repository as a ZIP file and extract it to your desired location.

---

## 💻 Usage

### Running the Python Script
```bash
python TicTacToe.py
```

### Running the Jupyter Notebook
```bash
jupyter notebook TicTacToe.ipynb
```

Then execute all cells in order to start the game.

---

## 🎮 How to Play

1. **Launch the game** - Run the script or notebook
2. **Click "PLAY GAME"** - Start a new game
3. **Select difficulty** - Choose Easy, Medium, or Hard
4. **Make your move** - Click on any empty cell
5. **Beat the AI** - Try to get three in a row!

### Controls
- **Reset Button** 🔄 - Restart the current game
- **Menu Button** 🏠 - Return to main menu
- **Play Again** - Start a new game with same difficulty
- **Main Menu** - Choose a different difficulty

---

## 🧠 How It Works

### 🎯 Game Algorithm Overview

The game implements three difficulty levels of artificial intelligence, each using a different strategy:

#### 1️⃣ **Easy Mode 😊**
```python
def easy_move(board_state):
    # Select a random empty cell
    choices = [i for i in range(9) if board_state[i] == ""]
    return random.choice(choices)
```
**Mechanism**: The AI makes completely random moves, perfect for beginners.

---

#### 2️⃣ **Medium Mode 🤔**
```python
def medium_move(board_state):
    # 30% random moves + 70% smart moves
    if random.random() < 0.3:
        choices = [i for i in range(9) if board_state[i] == ""]
        return random.choice(choices)
    return best_move_full(board_state)  # minimax
```
**Mechanism**: A balanced mix of random and strategic moves:
- 30% of the time it plays randomly
- 70% of the time it uses the Minimax algorithm
- This makes it challenging but still beatable

---

#### 3️⃣ **Hard Mode 😈 - Minimax Algorithm**

This is the ultimate challenge! It uses the **Minimax algorithm** which makes it **unbeatable** ✨

##### 📊 How Does the Minimax Algorithm Work?

```python
def minimax(board, depth, is_max):
    # 1. Check terminal states
    if check_win_for(board, "O"):  # AI wins
        return 1
    if check_win_for(board, "X"):  # Player wins
        return -1
    if "" not in board:            # Draw
        return 0
    
    # 2. Try all possible moves
    if is_max:  # AI's turn (maximize score)
        best = -infinity
        for each empty position:
            try move as "O"
            score = minimax(board, depth+1, False)
            undo move
            best = max(best, score)
        return best
    else:  # Player's turn (minimize AI's score)
        best = +infinity
        for each empty position:
            try move as "X"
            score = minimax(board, depth+1, True)
            undo move
            best = min(best, score)
        return best
```

##### 🔍 **Detailed Algorithm Explanation:**

**Core Principle:**
The algorithm explores all possible game outcomes until the end and selects the best move!

**Implementation Steps:**

1. **Base Cases (Terminal States)**:
   - If AI wins → return +1 (good for AI)
   - If player wins → return -1 (bad for AI)
   - If draw → return 0 (neutral)

2. **Maximizing Player (AI plays O)**:
   - Tries every empty cell
   - Evaluates each move recursively
   - Chooses the move that gives the highest score

3. **Minimizing Player (You play X)**:
   - The algorithm assumes you'll play optimally
   - Tries to minimize AI's winning chances
   - Chooses moves that reduce the AI's score

4. **Recursive Evaluation**:
   ```
   Current Board State
        ↓
   Try Move 1 → Explore all outcomes → Record score
   Try Move 2 → Explore all outcomes → Record score
   Try Move 3 → Explore all outcomes → Record score
        ↓
   Select best score
   ```

##### 🎮 **Practical Example:**

Suppose the board looks like this:
```
X | O |  
---------
  | X |  
---------
  |   | O
```

The AI (O) thinks:
1. Try each empty cell (0,2,3,5,6,7)
2. For each move, simulate all your possible responses
3. For each response, simulate its next move
4. Continue until reaching the game's end
5. Calculate the final score for each scenario
6. Choose the move that guarantees the best outcome

##### ⚡ **Best Move Selection:**

```python
def best_move_full(board_state):
    best_val = -infinity
    move = -1
    
    # Try each empty cell
    for i in range(9):
        if board_state[i] == "":
            board_state[i] = "O"           # Try the move
            move_val = minimax(...)        # Calculate its value
            board_state[i] = ""            # Undo the move
            
            if move_val > best_val:        # If better than previous
                best_val = move_val        # Save it
                move = i
    
    return move  # Return the best move
```

##### 🏆 **Why Is This Algorithm "Unbeatable"?**

- Explores **all possible game outcomes**
- Assumes you'll **always play optimally**
- Chooses moves that **guarantee the best result** even against perfect play
- In Tic Tac Toe, this means the AI can never lose
- The best you can achieve is a draw!

##### 📈 **Algorithm Complexity:**
- **Time Complexity**: O(9!) in worst case
- With **Alpha-Beta Pruning** it can be significantly reduced
- Tic Tac Toe is relatively small, so the algorithm runs very fast

---

### 🎯 **Difficulty Levels Summary:**

| Level | Strategy | Win Rate |
|-------|----------|----------|
| **Easy** 😊 | 100% Random moves | Very high for player |
| **Medium** 🤔 | 30% Random + 70% Smart | Moderate |
| **Hard** 😈 | 100% Minimax | Impossible to win! |

---

### 🧪 **Win Detection:**

```python
def check_win_for(board, player):
    # All possible winning combinations
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # Horizontal rows
        (0,3,6), (1,4,7), (2,5,8),  # Vertical columns
        (0,4,8), (2,4,6)             # Diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
```

---

## 🎨 Color Scheme

```python
Background:      #1a1a2e  # Dark navy
Secondary BG:    #16213e  # Darker navy
Accent:          #0f3460  # Deep blue
Button:          #e94560  # Vibrant red
Hover:           #ff6b81  # Light pink
X Color:         #00d9ff  # Cyan
O Color:         #ff6b81  # Pink
Text:            #eeeeee  # Light gray
```

---

## 📸 Screenshots

### Main Menu
```
⭕ TIC TAC TOE ❌
   Challenge the AI
   
   [🎮 PLAY GAME]
   [🚪 EXIT]
```

### Difficulty Selection
```
🎯 Select Difficulty

[😊 EASY]
[🤔 MEDIUM]
[😈 HARD]

[← BACK]
```

### Game Board
```
You: ❌  vs  AI: ⭕
😈 Hard Mode

┌───┬───┬───┐
│ X │ O │   │
├───┼───┼───┤
│   │ X │ O │
├───┼───┼───┤
│   │   │ X │
└───┴───┴───┘

[🔄 RESET]  [🏠 MENU]
```

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.7+ |
| GUI Framework | Tkinter |
| Algorithm | Minimax with Alpha-Beta Pruning |
| IDE Support | VS Code, PyCharm, Jupyter |

---

## 📁 Project Structure

```
TicTacToe-main/
│
├── TicTacToe.py          # Main Python script
├── TicTacToe.ipynb       # Jupyter Notebook version
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

---

## 🎯 Key Features Explained

### 1. **Minimax AI Algorithm**
- Evaluates all possible game states
- Chooses the optimal move
- Ensures AI never loses in Hard mode

### 2. **Modern GUI Design**
- Custom color scheme
- Hover effects on buttons
- Smooth transitions
- Emoji-enhanced interface

### 3. **Flexible Difficulty System**
- Adjustable AI intelligence
- Suitable for all skill levels
- Fair gameplay balance

---

## 🐛 Known Issues

None currently! Feel free to report any bugs in the Issues section.

---

## 👨‍💻 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🙏 Acknowledgments

- Minimax algorithm inspiration from game theory
- UI/UX design inspired by modern dark themes
- Built with using Python and Tkinter

