import os
import random
import nltk
from nltk.corpus import words, wordnet
import tkinter as tk
from tkinter import messagebox

# Download required datasets
nltk.download("words")
nltk.download("wordnet")

# Read words file once
try:
    with open("fiveletterwords_final.txt", "r") as f:
        valid_words = set(f.read().split())  # Store in a set for faster lookup
except FileNotFoundError:
    valid_words = set()  # If file not found, an empty set prevents crashes

#word_list = [word.lower() for word in words.words() if len(word) == 5]
word_list=list(valid_words)
class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle GUI")
        self.root.geometry("500x500")

        self.title_label = tk.Label(root, text="Wordle", font=("Helvetica", 20))
        self.title_label.pack(pady=5)

        # Labels for guesses
        self.l = [tk.Label(root, text="_ _ _ _ _", font=("Helvetica", 20)) for _ in range(5)]
        for label in self.l:
            label.pack(padx=10, pady=5)

        # Input field
        self.inp = tk.Entry(root)
        self.inp.pack(pady=20)

        # Error message label
        self.err = tk.Label(root, text="", fg="red")
        self.err.pack(pady=10)

        # Submit button
        self.submit_btn = tk.Button(root, text="Submit", command=self.wordle)
        self.submit_btn.pack(pady=10)

        self.reset_game()

    def reset_game(self):
        """ Resets the game state """
        self.answer = random.choice(word_list)
        self.guess_list = []
        self.err.config(text="")
        for label in self.l:
            label.config(text="_ _ _ _ _", fg="black")
        self.inp.delete(0, tk.END)
    
    def get_word_meaning(self, word):
        """ Fetches word meaning """
        synsets = wordnet.synsets(word)
        return synsets[0].definition() if synsets else "Meaning not found"

    def word_compare(self, guess):
        """ Compares guessed word with the answer and returns a formatted string """
        result = ""
        for i in range(5):
            if guess[i] == self.answer[i]:
                result += f" [{guess[i].upper()}] "  # Green
            elif guess[i] in self.answer:
                result += f" ({guess[i].upper()}) "  # Yellow
            else:
                result += f" {guess[i].upper()} "   # Red
        return result

    def wordle(self):
        """ Game logic handling user input """
        guess = self.inp.get().lower()

        if len(guess) != 5:
            self.err.config(text="Please enter a valid 5-letter word.")
            return

        if guess not in valid_words:
            self.err.config(text="Word not in list. Try again.")
            return

        row_no = len(self.guess_list)
        result = self.word_compare(guess)
        self.l[row_no].config(text=result)

        self.guess_list.append(guess)

        if guess == self.answer:
            messagebox.showinfo("Congratulations!", "You've guessed the word!")
            self.reset_game()
        elif len(self.guess_list) == 5:
            messagebox.showinfo("Game Over!", f"The word was: {self.answer}\nMeaning: {self.get_word_meaning(self.answer)}")
            self.reset_game()

# Initialize GUI
root = tk.Tk()
game = WordleGame(root)
root.mainloop()

