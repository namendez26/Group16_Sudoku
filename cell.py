class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    # TODO
    def set_sketched_value(self, value):
        # insert pygame stuff here

        # Once a cell is selected, the user can type a single-digit number to ‘sketch’ it in the cell (see the game-in-progress screenshot for an example).
        # If the selected cell has a sketched value, the user can press the return (enter) key to submit their guess.
        pass
    
    def draw(self):
        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected.
        pass
