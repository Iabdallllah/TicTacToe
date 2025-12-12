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

### Minimax Algorithm
The AI uses the **Minimax algorithm** for optimal decision-making in Hard mode:

```python
def minimax(board, depth, is_maximizing):
    # Evaluate terminal states
    if check_win(): return score
    
    # Recursively evaluate all possible moves
    if is_maximizing:
        return max(all_possible_moves)
    else:
        return min(all_possible_moves)
```

### Difficulty Levels
- **Easy**: `random.choice(available_moves)`
- **Medium**: 30% random + 70% minimax
- **Hard**: 100% minimax (unbeatable)

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

## 🔮 Future Enhancements

- [ ] Two-player mode
- [ ] Game statistics tracking
- [ ] Sound effects
- [ ] Animation effects for wins
- [ ] Themes customization
- [ ] Multiplayer online mode

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
- Built with ❤️ using Python and Tkinter

---

<div align="center">

**Made with ❤️ and Python**

⭐ Star this repo if you like it!

</div>