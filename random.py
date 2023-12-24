import tkinter as tk
from tkinter import ttk
import random

class RandomNumberGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Generator")

        self.label = ttk.Label(root, text="Random Number:")
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(root, textvariable=self.result_var)

        self.generate_button = ttk.Button(root, text="Generate Random Number", command=self.generate_random_number)

        self.label.pack(pady=10)
        self.result_label.pack(pady=10)
        self.generate_button.pack(pady=10)

    def generate_random_number(self):
        random_integer = random.randint(1, 10)
        self.result_var.set(str(random_integer))

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGeneratorApp(root)
    root.mainloop()