#password guessing game
# import random

# easy_words= ["python","train", "plane", "tram", "auto"]
# medium_words = ["apple", "grape", "peach", "mango", "lemon"]
# hard_words =["elephant", "giraffe", "dolphine", "kangroo", "alligator"]

# print("Welcome to the Password Guessing Game!")
# print("Choose difficulty level: easy, medium, hard")

# level = input("Enter Difficulty:  ").lower()
# if level == "easy":
#     secret_words =random.choice(easy_words)
# elif level == "medium":
#     secret_words =random.choice(medium_words)
# elif level == "hard":
#     secret_words =random.choice(hard_words)

# else:
#     print("Invalid level. Defaulting to easy.")
#     secret_words =random.choice(easy_words)

# attempts = 0
# print("Guess the word!")
# while True:
#     guess = input("Enter your guess: ").lower()
#     attempts += 1

#     if guess == secret_words:
#         print(f"Congratulations! You've guessed the word '{secret_words}' in {attempts} attempts.")
#         break

#     hint = ""
#     for i in range(len(secret_words)):
#         if i < len(guess) and guess[i] == secret_words[i]:
#             hint += guess[i]
#         else:
#             hint +="_"

#     print("Hint: " , hint)

# print("Game over. Thanks For Playing!")

import tkinter as tk
import random
from tkinter import messagebox

# Word lists
easy_words = ["python", "train", "plane", "tram", "auto"]
medium_words = ["apple", "grape", "peach", "mango", "lemon"]
hard_words = ["elephant", "giraffe", "dolphin", "kangaroo", "alligator"]

# Initialize variables
secret_word = ""
attempts = 0

# --- FUNCTIONS ---

def set_difficulty(level):
    global secret_word, attempts
    attempts = 0

    if level == "easy":
        secret_word = random.choice(easy_words)
    elif level == "medium":
        secret_word = random.choice(medium_words)
    elif level == "hard":
        secret_word = random.choice(hard_words)

    result_label.config(text=f"Difficulty set to {level.capitalize()}! Start guessing...")
    hint_label.config(text="")
    attempts_label.config(text="Attempts: 0")
    entry.delete(0, tk.END)


def check_guess():
    global attempts
    guess = entry.get().lower()

    if not secret_word:
        messagebox.showinfo("Info", "Please select a difficulty first!")
        return

    if not guess:
        messagebox.showwarning("Warning", "Please enter a guess!")
        return

    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")

    if guess == secret_word:
        messagebox.showinfo("🎉 Congratulations", f"You guessed '{secret_word}' in {attempts} attempts!")
        reset_game()
        return

    # Generate hint
    hint = ""
    for i in range(len(secret_word)):
        if i < len(guess) and guess[i] == secret_word[i]:
            hint += guess[i]
        else:
            hint += "_"

    hint_label.config(text=f"Hint: {hint}")
    result_label.config(text="❌ Wrong guess! Try again.")


def reset_game():
    global secret_word, attempts
    secret_word = ""
    attempts = 0
    hint_label.config(text="")
    result_label.config(text="Game reset! Choose difficulty again.")
    attempts_label.config(text="Attempts: 0")
    entry.delete(0, tk.END)


# --- GUI SETUP ---

root = tk.Tk()
root.title("Password Guessing Game")
root.geometry("420x380")
root.resizable(False, False)
root.config(bg="#f0f4f7")

title_label = tk.Label(root, text="🔐 Password Guessing Game", font=("Arial", 16, "bold"), bg="#f0f4f7", fg="#2c3e50")
title_label.pack(pady=10)

# Difficulty buttons
difficulty_frame = tk.Frame(root, bg="#f0f4f7")
difficulty_frame.pack()

tk.Label(difficulty_frame, text="Select Difficulty:", bg="#f0f4f7").pack(side="left", padx=5)

tk.Button(difficulty_frame, text="Easy", width=8, command=lambda: set_difficulty("easy")).pack(side="left", padx=5)
tk.Button(difficulty_frame, text="Medium", width=8, command=lambda: set_difficulty("medium")).pack(side="left", padx=5)
tk.Button(difficulty_frame, text="Hard", width=8, command=lambda: set_difficulty("hard")).pack(side="left", padx=5)

# Guess input
entry = tk.Entry(root, font=("Arial", 14), width=20, justify="center")
entry.pack(pady=15)

tk.Button(root, text="Check Guess", font=("Arial", 12), bg="#4CAF50", fg="white", command=check_guess).pack(pady=5)
tk.Button(root, text="Reset Game", font=("Arial", 10), bg="#e74c3c", fg="white", command=reset_game).pack(pady=5)

# Live attempt counter
attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 12, "bold"), bg="#f0f4f7", fg="#2c3e50")
attempts_label.pack(pady=5)

# Hint and result labels
hint_label = tk.Label(root, text="", font=("Consolas", 14), bg="#f0f4f7", fg="#34495e")
hint_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f4f7", fg="#2c3e50")
result_label.pack(pady=5)

root.mainloop()
