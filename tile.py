from tkinter import Button

class Tile(Button):
    '''
    Button that act as the tiles for the game
    '''
    def __init__(self, parent, row, column, piece, color):
        super(Tile, self).__init__(
            parent,
            height=46,
            width=46,
            bd=0,
            image=piece.image,
            command=self.print_position,
            background=color
        )
        self.row = row
        self.column = column
        self.piece = piece

    def print_position(self):
        print(f"{self.row} {self.column}")
        print(f"image: {self.piece.image}")
