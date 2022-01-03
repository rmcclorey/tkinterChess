from tkinter import Button

class Tile(Button):
    '''
    Button that act as the tiles for the game
    '''
    def __init__(self, parent, row, column, piece, color):
        super(Tile, self).__init__(parent, height=2, width=2, bd=0, command=self.print_position, background=color)
        self.row = row
        self.column = column
        self.piece = piece

    def print_position(self):
        print(f"{self.row} {self.column}")
