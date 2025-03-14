import tkinter as tk
from lexer import Lexer
from utils import read_file

class LexerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")

        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack()

        self.button = tk.Button(root, text="Analizar", command=self.run_lexer)
        self.button.pack()

        self.result_area = tk.Text(root, height=10, width=50)
        self.result_area.pack()

    def run_lexer(self):
        text = self.text_area.get("1.0", tk.END)
        lexer = Lexer(text)
        tokens = lexer.tokenize()
        self.result_area.delete("1.0", tk.END)
        for token in tokens:
            self.result_area.insert(tk.END, f"{token}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = LexerGUI(root)
    root.mainloop()
