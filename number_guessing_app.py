import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🎯 Number Guessing Game", 
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Instructions
        instruction_label = tk.Label(
            self.root,
            text="Guess the number between 1 and 100!",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        instruction_label.pack(pady=10)
        
        # Attempts display
        self.attempts_label = tk.Label(
            self.root,
            text=f"Attempts: {self.attempts}/{self.max_attempts}",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#007acc"
        )
        self.attempts_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=20)
        
        # Entry field
        self.guess_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=10,
            justify="center"
        )
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.bind("<Return>", self.make_guess)
        
        # Submit button
        submit_btn = tk.Button(
            input_frame,
            text="Guess!",
            font=("Arial", 12, "bold"),
            bg="#007acc",
            fg="white",
            command=self.make_guess,
            relief=tk.FLAT,
            padx=20
        )
        submit_btn.pack(side=tk.LEFT, padx=5)
        
        # Feedback display
        self.feedback_label = tk.Label(
            self.root,
            text="Enter your guess above!",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333",
            wraplength=350
        )
        self.feedback_label.pack(pady=20)
        
        # New game button
        self.new_game_btn = tk.Button(
            self.root,
            text="🔄 New Game",
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            command=self.new_game,
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        self.new_game_btn.pack(pady=10)
        self.new_game_btn.config(state=tk.DISABLED)
        
    def make_guess(self, event=None):
        try:
            guess = int(self.guess_entry.get())
            
            if not 1 <= guess <= 100:
                self.feedback_label.config(
                    text="❌ Please enter a number between 1 and 100!",
                    fg="#dc3545"
                )
                return
                
        except ValueError:
            self.feedback_label.config(
                text="❌ Please enter a valid number!",
                fg="#dc3545"
            )
            return
            
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        
        if guess == self.secret:
            self.feedback_label.config(
                text=f"🎉 Congratulations! You guessed it in {self.attempts} attempts!",
                fg="#28a745"
            )
            self.game_over()
        elif guess < self.secret:
            self.feedback_label.config(
                text=f"📈 Too low! Try a higher number.",
                fg="#ffc107"
            )
        else:
            self.feedback_label.config(
                text=f"📉 Too high! Try a lower number.",
                fg="#ffc107"
            )
            
        self.guess_entry.delete(0, tk.END)
        
        if self.attempts >= self.max_attempts and guess != self.secret:
            self.feedback_label.config(
                text=f"😔 Game Over! The number was {self.secret}",
                fg="#dc3545"
            )
            self.game_over()
            
    def game_over(self):
        self.guess_entry.config(state=tk.DISABLED)
        self.new_game_btn.config(state=tk.NORMAL)
        
    def new_game(self):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.feedback_label.config(
            text="Enter your guess above!",
            fg="#333333"
        )
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)
        self.new_game_btn.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
