import tkinter as tk

from tile import Tile
from piece import Pawn, King

class Board(tk.Frame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.tiles = []
        self.make_board()

    def make_board(self)->None:
        '''
        creates and initializes chess board.
        Takes Tk root object to add the buttons to, and returns an array representing the board
        '''
        for x in range(0,8):
            for y in range(0,8):
                #set colors to checkerboard
                color = 'black'
                if (x+y) % 2 == 0:
                    color='white'

                self.tiles.append(Tile(self, x, y, King(x,y), color))

    def update_board(self)->None:
        '''
        Loops through all boards and updates them
        '''
        for tile in self.tiles:
            tile.grid(row=tile.row, column=tile.column)
