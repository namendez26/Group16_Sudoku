class SudokuGenerator():
    
    def __init__ (self, row_length, removed_cells):
        '''
        __init__(self, row_length, removed_cells)
        Constructor for the SudokuGenerator class.
        For the purposes of this project, row_length is always 9.
        removed_cells could vary depending on the difficulty level chosen (see UI Requirements).
        '''
        self.row_length = 9
        if SudokuGenerator().difficulty == "easy":
            self.removed_cells = 30
        elif SudokuGenerator().difficulty == "medium":
            self.removed_cells = 40
        elif SudokuGenerator().difficulty == "hard":
            self.removed_cells = 50
    
    def get_board(self):
        pass
    def print_board(self):
        '''
        Displays the board to the console.
        This is not strictly required, but it may be useful for debugging purposes.
        '''
        pass
    def valid_in_row(self, row, num):
        '''
        Returns a Boolean value.
        Determines if num is contained in the given row of the board.
        '''
        pass
    def valid_in_col(self, col, num):
        '''
        Returns a Boolean value.
        Determines if num is contained in the given column of the board.
        '''
        pass
    def valid_in_box(self, row_start, col_start, num):
        '''
        Returns a Boolean value.
        Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
        '''
        pass
    def is_valid(self, row, col, num):
        '''
        Returns if it is valid to enter num at (row, col) in the board.
        This is done by checking the appropriate row, column, and box.
        '''
        pass
    def fill_box(self, row_start, col_start):
        '''
        Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
        Uses unused_in_box to ensure no value occurs in the box more than once.
        '''
        pass
    def fill_diagonal(self):
        '''
        Fills the three boxes along the main diagonal of the board.
        This is the first major step in generating a Sudoku.
        See the Step 1 picture in Sudoku Generation for further explanation.
        fill_remaining(self, row, col)
        This method is provided for students.
        It is the second major step in generating a Sudoku.
        This will return a completely filled board (the Sudoku solution).
        '''
        pass
    def fill_values(self):
        '''
        This method is provided for students.
        It constructs a solution by calling fill_diagonal and fill_remaining.
        '''
        pass
    def remove_cells(self):
        '''
        This method removes the appropriate number of cells from the board.
        It does so by randomly generating (row, col) coordinates of the board and setting the value to 0.
        Note: Be careful not to remove the same cell multiple times. A cell can only be removed once.
        This method should be called after generating the Sudoku solution.
        '''
        pass
    def generate_sudoku(size, removed):
        '''
        Note: This is a function outside of the SudokuGenerator class.
        This function should also be implemented in sudoku_generator.py as it interacts with the class.
        Given size and removed, this function generates and returns a size-by-size sudoku board.
        The board has cleared removed number of cells.
        This function should just call the constructor and appropriate methods from the SudokuGenerator class.
        '''
        pass

class Cell():

    def __init__(self, value, row, col, screen):
        '''
        Constructor for the Cell class
        '''
        pass
    def set_cell_value(self, value):
        '''
        Setter for this cell’s value
        '''
        pass
    def set_sketched_value(self, value):
        '''
        Setter for this cell’s sketched value
        '''
        pass
    def draw(self):
        '''
        Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected.
        '''
        pass

class Board():
    def __init__(self, width, height, screen, difficulty):
        '''
        Constructor for the Board class.
        screen is a window from PyGame.
        difficulty is a variable to indicate if the user chose easy, medium, or hard.
        '''
        pass
    def draw(self):
        '''
        Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board.
        '''
        pass
    def select(self, row, col):
        '''
        Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value.
        '''
        pass
    def click(self, x, y):
        '''
        If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        of the cell which was clicked. Otherwise, this function returns None.
        '''
        pass
    def clear(self):
        '''
        Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves.
        '''
        pass
    def sketch(self, value):
        '''
        Sets the sketched value of the current selected cell equal to user entered value.
        It will be displayed at the top left corner of the cell using the draw() function.
        '''
        pass
    def place_number(self, value):
        '''
        Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key.
        '''
        pass
    def reset_to_original(self):
        '''
        Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        '''
    def is_full(self):
        '''
        Returns a Boolean value indicating whether the board is full or not.
        '''
        pass
    def update_board(self):
        '''
        Updates the underlying 2D board with the values in all cells.
        '''
        pass
    def find_empty(self):
        '''
        Finds an empty cell and returns its row and col as a tuple (x, y).
        '''
        pass
    def check_board(self):
        '''
        Check whether the Sudoku board is solved correctly.    
        '''
        pass