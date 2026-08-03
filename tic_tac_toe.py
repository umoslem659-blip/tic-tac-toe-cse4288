S"""
CSE4288 - 9F Graphics Lab
Offline 2 Player Game: Tic-Tac-Toe

Student 1 Name: Md moslem uddin| ID: 41220100153
Student 2 Name: nur alam | ID: 41220100126
"""

import tkinter as tk
from tkinter import messagebox

# ---------- Game State ----------
board = [""] * 9          # 9 cells, index 0-8
current_player = "X"      # X always starts
buttons = []               # will hold button widgets
game_over = False

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6)               # diagonals
]

PLAYER_COLORS = {"X": "#1976D2", "O": "#D32F2F"}


def check_winner():
    """Return 'X', 'O' if someone won, 'Draw' if board full, else None."""
    for a, b, c in WIN_COMBOS:
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a], (a, b, c)
    if "" not in board:
        return "Draw", None
    return None, None


def on_click(index):
    global current_player, game_over

    if game_over or board[index] != "":
        return  # cell already taken or game finished

    board[index] = current_player
    buttons[index].config(
        text=current_player,
        fg=PLAYER_COLORS[current_player],
        disabledforeground=PLAYER_COLORS[current_player]
    )

    result, combo = check_winner()

    if result == "Draw":
        game_over = True
        status_label.config(text="It's a Draw!")
        messagebox.showinfo("Game Over", "It's a Draw!")
    elif result in ("X", "O"):
        game_over = True
        for i in combo:
            buttons[i].config(bg="#A5D6A7")  # highlight winning cells
        status_label.config(text=f"Player {result} Wins!")
        messagebox.showinfo("Game Over", f"Player {result} Wins!")
    else:
        current_player = "O" if current_player == "X" else "X"
        status_label.config(
            text=f"Player {current_player}'s Turn",
            fg=PLAYER_COLORS[current_player]
        )


def restart_game():
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False
    for btn in buttons:
        btn.config(text="", bg="#FFFFFF")
    status_label.config(text="Player X's Turn", fg=PLAYER_COLORS["X"])


# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Tic-Tac-Toe - Offline 2 Player Game")
root.resizable(False, False)
root.configure(bg="#ECEFF1")

title_label = tk.Label(
    root, text="Tic-Tac-Toe", font=("Helvetica", 22, "bold"),
    bg="#ECEFF1", fg="#37474F", pady=10
)
title_label.grid(row=0, column=0, columnspan=3)

status_label = tk.Label(
    root, text="Player X's Turn", font=("Helvetica", 14, "bold"),
    bg="#ECEFF1", fg=PLAYER_COLORS["X"], pady=5
)
status_label.grid(row=1, column=0, columnspan=3)

board_frame = tk.Frame(root, bg="#ECEFF1")
board_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

for i in range(9):
    btn = tk.Button(
        board_frame, text="", font=("Helvetica", 32, "bold"),
        width=4, height=2, bg="#FFFFFF",
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i // 3, column=i % 3, padx=3, pady=3)
    buttons.append(btn)

restart_button = tk.Button(
    root, text="Restart Game", font=("Helvetica", 12, "bold"),
    bg="#37474F", fg="white", command=restart_game, pady=6
)
restart_button.grid(row=3, column=0, columnspan=3, pady=(0, 15), sticky="we", padx=15)

root.mainloop()
