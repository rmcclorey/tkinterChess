#!/usr/bin/env python3
import tkinter as tk
from board import Board

#if run directly, create the board and run the tkinter mainloop
if __name__=='__main__':
    root = tk.Tk()
    root.title("Chess!")
    main_board = Board(root)
    main_board.make_board()
    main_board.update_board()
    main_board.pack()
    root.mainloop()
