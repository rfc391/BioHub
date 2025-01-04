
import tkinter as tk
from tkinter import messagebox
from src.trello_manager import TrelloManager

class TrelloAutomationGUI:
    def __init__(self):
        self.trello = TrelloManager()
        self.root = tk.Tk()
        self.root.title("Trello Automation")

        # Create GUI elements
        self.board_label = tk.Label(self.root, text="Board Name:")
        self.board_label.pack()
        self.board_entry = tk.Entry(self.root, width=30)
        self.board_entry.pack()

        self.create_board_button = tk.Button(self.root, text="Create Board", command=self.create_board)
        self.create_board_button.pack()

        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.pack()

    def create_board(self):
        board_name = self.board_entry.get()
        if not board_name:
            messagebox.showerror("Error", "Board name cannot be empty!")
            return
        try:
            board = self.trello.create_board(board_name)
            self.status_label.config(text=f"Board '{board.name}' created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create board: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = TrelloAutomationGUI()
    gui.run()
