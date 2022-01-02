#!/usr/bin/env python3
import tkinter as tk

def button_action():
    print('pressed')

def make_board(root:tk.Tk)->None:
    for num in range(8,0,-1):
        for letter in range(ord('a'),ord('i')):
            label=f"{chr(letter)}{num}"
            tmp = tk.Button(root, text=label, command=button_action, height=2, width=2, bd=0)
            tmp.grid(row=letter-ord('a'),column=num)

if __name__=='__main__':
    root = tk.Tk()
    root.title("Chess!")
    make_board(root)
    root.mainloop()
