# Artificial Intelligence Lab: Tic-Tac-Toe AI

A Python-based terminal game of **Tic-Tac-Toe featuring an unbeatable AI opponent** powered by the **Minimax Algorithm**. This project demonstrates fundamental game theory and adversarial search techniques for AI Lab submissions.

---

## 🚀 Features
- **Unbeatable AI**: Powered by the recursive Minimax algorithm, ensuring the AI never loses (guarantees either an AI win or a strategic draw).
- **Zero Dependencies**: Built strictly using standard Python libraries (`math`).
- **Interactive CLI**: Simple 1–9 input mapping corresponding to grid positions.

---

## 📊 Core Concepts & Algorithm
The **Minimax algorithm** is a backtracking strategy used in decision-making and game theory. It operates under a zero-sum framework assuming optimal play from both sides:
- **Maximizing Player (AI - 'O')**: Aims to choose the path that yields the highest score.
- **Minimizing Player (Human - 'X')**: Aims to force the AI into paths with the lowest score.
- **Terminal States**: Scores are weighted by depth (`10 - depth`) to favor winning sooner and losing later.

---

## 🛠️ Project Structure & Code

Save the following code as `tictactoe.py`:

```python
import math

# Initialize the 3x3 board
board = [" " for _ in range(9)]
PLAYER_X = "X"  # Human
PLAYER_O = "O"  # AI


def print_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} \n")


def check_winner(b, mark):
    win_conditions = [,
 ,
 ,  # Rows,
 ,
 ,  # Columns,
 ,  # Diagonals
    ]
    return any(
        all(b[pos] == mark for pos in condition) for condition in win_conditions
    )


def is_draw(b):
    return " " not in b


def get_empty_indices(b):
    return [i for i, spot in enumerate(b) if spot == " "]


# Minimax Algorithm for AI (Player O)
def minimax(b, depth, is_maximizing):
    if check_winner(b, PLAYER_O):
        return 10 - depth
    if check_winner(b, PLAYER_X):
        return depth - 10
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in get_empty_indices(b):
            b[i] = PLAYER_O
            score = minimax(b, depth + 1, False)
            b[i] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in get_empty_indices(b):
            b[i] = PLAYER_X
            score = minimax(b, depth + 1, True)
            b[i] = " "
            best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = None
    for i in get_empty_indices(board):
        board[i] = PLAYER_O
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    board[move] = PLAYER_O


def player_move():
    while True:
        try:
            choice = int(input("Enter your move (1-9): ")) - 1
            if choice in get_empty_indices(board):
                board[choice] = PLAYER_X
                break
            else:
                print("Invalid or occupied position. Try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")


def play_game():
    print("Welcome to Tic-Tac-Toe AI Lab!")
    print_board([str(i + 1) for i in range(9)])

    while True:
        player_move()
        print_board(board)
        if check_winner(board, PLAYER_X):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        print_board(board)
        if check_winner(board, PLAYER_O):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
```

---

## 💻 How to Use

### 1. Requirements
- Python 3.6 or higher.

### 2. Run Command
Execute the script via your command line interface:
```bash
python tictactoe.py
```

### 3. Grid Mechanics
Input your moves selecting numbers **1 to 9** corresponding to the mapping layout below:
```text
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
```
