# 🎮 XO Game - Alpha-Beta Pruning AI

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Alpha--Beta%20Pruning-red.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Console-based Tic Tac Toe with unbeatable AI using Alpha-Beta Pruning**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [How It Works](#-how-it-works)

</div>

---

## ✨ Features

### 💻 **Console Interface**
- Clean command-line interface
- Simple text-based board visualization
- Fast and efficient gameplay
- Perfect for terminal enthusiasts
- No GUI dependencies required

### 🤖 **Intelligent AI**
- **Alpha-Beta Pruning algorithm** for optimal performance
- **Unbeatable AI opponent** - best you can achieve is a draw!
- Faster than standard Minimax
- Optimized game tree search with branch pruning

### 🎯 **Gameplay Features**
- Single-player vs AI
- Real-time move validation
- Win/Draw detection
- Clear position indicators (0-8)
- Automatic game restart after each round

---

## 📋 Requirements

- **Python 3.7 or higher**
- No external dependencies needed!

---

## 🚀 Installation

### Option 1: Clone the Repository
```bash
git clone https://github.com/Iabdallllah/TicTacToe.git
cd TicTacToe
```

### Option 2: Download ZIP
Download the repository as a ZIP file and extract it to your desired location.

---

## 💻 Usage

### Running the Console Game
```bash
python XO_Console.py
```

**How to Play:**
1. **Launch the game** - Run the script
2. **Enter position** - Type a number from 0-8 to place your move
3. **AI responds** - The AI will make its optimal move
4. **Try to win** - Good luck beating the Alpha-Beta AI!

**Board Positions:**
```
 0 | 1 | 2
 3 | 4 | 5
 6 | 7 | 8
```

**Example Gameplay:**
```
========================================
XO Game with Alpha-Beta Pruning
========================================
You are O, AI is X
Board positions: 0-8

 0 | 1 | 2
 3 | 4 | 5
 6 | 7 | 8

-------------
|   |   |   |
-------------

Enter position (0-8): 4
```

---

## 🧠 How It Works

### 🎯 Alpha-Beta Pruning Algorithm

The game uses the **Alpha-Beta Pruning algorithm**, an optimized version of Minimax that makes the AI unbeatable while being faster and more efficient.

##### 📊 How Does Alpha-Beta Pruning Work?

```python
def alpha_beta(board, depth, maximizing, alpha, beta):
    # 1. Check terminal states
    if check_winner(board, "X"):  # AI wins
        return 1
    if check_winner(board, "O"):  # Player wins
        return -1
    if is_full(board):            # Draw
        return 0
    
    # 2. Try possible moves with pruning
    if maximizing:  # AI's turn (maximize score)
        best = -10000
        for each empty position:
            try move as "X"
            score = alpha_beta(board, depth+1, False, alpha, beta)
            undo move
            best = max(best, score)
            alpha = max(alpha, best)
            if alpha >= beta:  # Prune! Skip remaining branches
                break
        return best
    else:  # Player's turn (minimize AI's score)
        best = 10000
        for each empty position:
            try move as "O"
            score = alpha_beta(board, depth+1, True, alpha, beta)
            undo move
            best = min(best, score)
            beta = min(beta, best)
            if alpha >= beta:  # Prune! Skip remaining branches
                break
        return best
```

##### 🔍 **Detailed Algorithm Explanation:**

**Core Principle:**
Alpha-Beta Pruning explores game outcomes like Minimax but **skips branches that won't affect the final decision**, making it much faster!

**Implementation Steps:**

1. **Base Cases (Terminal States)**:
   - If AI (X) wins → return +1 (good for AI)
   - If Player (O) wins → return -1 (bad for AI)
   - If draw → return 0 (neutral)

2. **Maximizing Player (AI plays X)**:
   - Tries every empty cell
   - Evaluates each move recursively
   - Chooses the move that gives the highest score
   - Updates `alpha` (best value for maximizer)

3. **Minimizing Player (You play O)**:
   - The algorithm assumes you'll play optimally
   - Tries to minimize AI's winning chances
   - Chooses moves that reduce the AI's score
   - Updates `beta` (best value for minimizer)

4. **Pruning Step (Key Optimization)**:
   - If `alpha >= beta`, stop exploring this branch
   - We already found a better option elsewhere
   - This saves computation time!

5. **Recursive Evaluation with Pruning**:
   ```
   Current Board State
        ↓
   Try Move 1 → Explore outcomes → Record score → Update alpha/beta
   Try Move 2 → Explore outcomes → Record score → Check pruning
        ↓
   If alpha >= beta: STOP! (Prune remaining moves)
   Otherwise: Continue exploring
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

The AI (X) thinks:
1. Try each empty cell (positions 2, 3, 5, 6, 7)
2. For each move, simulate all your possible responses
3. For each response, simulate its next move
4. **If it finds a guaranteed win, prune other branches** ✂️
5. Calculate the final score for each scenario
6. Choose the move that guarantees the best outcome

**Pruning Example:**
```
        AI's turn
       /    |    \
      3     8    Win! → Score: +1
     /       
   [more exploration...]  ← PRUNED! No need to check
```
Once we find a winning move, we don't need to explore worse options!

##### ⚡ **Best Move Selection:**

```python
def best_move():
    best_val = -10000
    move = -1
    
    # Try each empty cell
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"           # Try the move
            val = alpha_beta(board, 0, False, -10000, 10000)
            board[i] = " "           # Undo the move
            
            if val > best_val:       # If better than previous
                best_val = val       # Save it
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

**Standard Minimax:**
- **Time Complexity**: O(b^d) where b = branching factor, d = depth
- For Tic Tac Toe: O(9!) ≈ 362,880 nodes in worst case

**With Alpha-Beta Pruning:**
- **Best Case**: O(b^(d/2)) - cuts search space in half!
- **Average Case**: Significantly faster than Minimax
- **Worst Case**: O(b^d) - same as Minimax (rare)

**In Practice:**
- Tic Tac Toe is small, so both are very fast
- Alpha-Beta pruning still provides noticeable speedup
- Perfect for real-time gameplay!

---

### 📊 **Alpha-Beta vs Minimax Comparison:**

| Feature | Minimax | Alpha-Beta Pruning |
|---------|---------|-------------------|
| **Explores all nodes** | ✅ Yes | ❌ No (prunes) |
| **Time Complexity** | O(b^d) | O(b^(d/2)) best case |
| **Optimal Solution** | ✅ Yes | ✅ Yes |
| **Speed** | Slower | Faster ⚡ |
| **Memory** | Same | Same |
| **Implementation** | Simpler | Slightly more complex |

**Winner:** Alpha-Beta Pruning (Same results, better performance!)

---

### 🧪 **Win Detection:**

```python
def check_winner(board, player):
    # All possible winning combinations
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],  # Horizontal rows
        [0,3,6], [1,4,7], [2,5,8],  # Vertical columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for s in win_states:
        if board[s[0]] == board[s[1]] == board[s[2]] == player:
            return True
    return False
```
---

## 📸 Example Gameplay

### Console Output
```
========================================
XO Game with Alpha-Beta Pruning
========================================
You are O, AI is X
Board positions: 0-8

 0 | 1 | 2
 3 | 4 | 5
 6 | 7 | 8

-------------
|   |   |   |
|   |   |   |
|   |   |   |
-------------

Enter position (0-8): 4

-------------
|   |   |   |
|   | O |   |
|   |   |   |
-------------

AI is thinking...

-------------
|   |   |   |
|   | O | X |
|   |   |   |
-------------

Enter position (0-8): 
```

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.7+ |
| Interface | Console/Terminal |
| Algorithm | Alpha-Beta Pruning |
| Dependencies | None (Pure Python) |
| IDE Support | VS Code, PyCharm, Any Terminal |

---

## 📁 Project Structure

```
TicTacToe/
│
├── XO_Console.py         # Console game with Alpha-Beta Pruning
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

---

## 🎯 Key Features

### **Alpha-Beta Pruning Algorithm**
- **Optimized version of Minimax**
- Prunes unnecessary branches in the game tree
- **Faster computation** while maintaining optimal play
- Reduces time complexity from O(b^d) to O(b^(d/2)) in best case
- **Unbeatable AI** - best you can achieve is a draw!

### **Algorithm Advantages**
1. **Same Results as Minimax** - Finds the exact same optimal move
2. **Better Performance** - Explores fewer nodes
3. **Efficient Pruning** - Skips branches that won't affect the outcome
4. **Real-time Response** - Fast enough for instant gameplay

### **Game Features**
- Clean command-line interface
- Clear position indicators (0-8)
- Real-time move validation
- Win/Draw detection
- Automatic game restart

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
