import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

class SmolPad(KMKKeyboard):
    def __init__(self):
        super().__init__()

       
        self.col_pins = (board.D0, board.D1, board.D2)
        self.row_pins = (board.D3, board.D4, board.D5)

       
        self.diode_orientation = DiodeOrientation.COL2ROW

        
        self.coord_mapping = [
            0, 1, 2,  
            3, 4, 5,  
            6, 7, 8,  
        ]
