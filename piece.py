from tkinter import PhotoImage

class Piece():
    '''
    Piece baseclass
    '''
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

class Pawn(Piece):
    def __init__(self, xPos, yPos):
        super(Pawn, self).__init__(xPos, yPos)
        self.image = PhotoImage(file="./images/blk_pawn.png")

    def get_move(self):
        pass

class Rook(Piece):
    def __init__(self, xPos, yPos):
        super(Rook, self).__init__(xPos, yPos)
        self.image = PhotoImage(file="./images/blk_rook.png")

    def get_move(self):
        pass

class Knight(Piece):
    def __init__(self, xPos, yPos):
        super(Knight, self).__init__(xPos, yPos)
        self.image = PhotoImage(file="./images/blk_knight.png")

    def get_move(self):
        pass

class Bishop(Piece):
    def __init__(self, xPos, yPos):
        super(Bishop, self).__init__(xPos, yPos)
        self.image = PhotoImage(file="./images/blk_bishop.png")

    def get_move(self):
        pass

class King(Piece):
    def __init__(self, xPos, yPos):
        super(King, self).__init__(xPos, yPos)
        self.image = PhotoImage(file="./images/blk_king.png")

    def get_move(self):
        pass

class Queen(Piece):
    def __init__(self, xPos, yPos):
        super(Queen, self).__init__(xPos, yPos)
        self.image = PhotoImage(file="./images/blk_queen.png")

    def get_move(self):
        pass
