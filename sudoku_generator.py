import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""

class SudokuGenerator:
    '''
    create a sudoku board - initialize class variables and set up the 2D board
    This should initialize:
    self.row_length      - the length of each row
    self.removed_cells  - the total number of cells to be removed
    self.board          - a 2D list of ints to represent the board
    self.box_length     - the square root of row_length

    Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

    Return:
    None
    '''
    def __init__(self, row_length = 9, removed_cells = 30):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * self.row_length for _ in range(self.row_length)]
        self.box_length = int(math.sqrt(row_length))
        
    '''
    Returns a 2D python list of numbers which represents the board

    Parameters: None
    Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
    Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

    Parameters: None
    Return: None
    '''
    def print_board(self):
        for row in self.board:
            print(row)

    '''
    Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

    Parameters:
    row is the index of the row we are checking
    num is the value we are looking for in the row
    
    Return: boolean
    '''
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    '''
    Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

    Parameters:
    col is the index of the column we are checking
    num is the value we are looking for in the column
    
    Return: boolean
    '''
    def valid_in_col(self, col, num):
        return num not in [row[col] for row in self.board]

    '''
    Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    num is the value we are looking for in the box

    Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

    Parameters:
    row and col are the row index and col index of the cell to check in the board
    num is the value to test if it is safe to enter in this cell

    Return: boolean
    '''
    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num))


    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

    Return: None
    '''
    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        for i in range(self.box_length):
            for j in range(self.box_length):
                while True:
                    num = nums.pop()
                    if self.is_valid(row_start + i, col_start + j, num):
                        self.board[row_start + i][col_start + j] = num
                        break


    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

    Parameters: None
    Return: None
    '''
    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)



    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
    
    Parameters:
    row, col specify the coordinates of the first empty (0) cell

    Return:
    boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
    # If we have reached the end of a row, move to the next row
    # If the current row is the last row, return True (indicating completion)
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        
        # Adjust col and row indices to start filling from the next box
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            # If we are in the last row of the box, move to the next row and reset col
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                # If we have reached the end of the board, return True (indicating completion)
                if row >= self.row_length:
                    return True

        # Attempt to fill the current cell with numbers 1 to row_length
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                # If the current number is valid, set it in the board
                self.board[row][col] = num
                # Recursively try to fill the next cell
                if self.fill_remaining(row, col + 1):
                    return True
                # If the attempt fails, reset the current cell to 0 and try the next number
                self.board[row][col] = 0
        # If none of the numbers work for the current cell, return False (backtrack)
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

    Parameters: None
    Return: None
    '''
    def fill_values(self):
        # Fill the diagonal boxes first
        self.fill_diagonal()
        # Start filling the remaining cells after the diagonal boxes have been filled
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

    Parameters: None
    Return: None
    '''
    def remove_cells(self):
        cells = [(i, j) for i in range(self.row_length) for j in range(self.row_length)]
        random.shuffle(cells)
        for _ in range(self.removed_cells):
            row, col = cells.pop()
            self.board[row][col] = 0



'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    # Create a SudokuGenerator object with specified size and number of cells to remove
    sudoku = SudokuGenerator(size, removed)
    # Fill the Sudoku board with values
    sudoku.fill_values()
    # Get the filled Sudoku board
    board = sudoku.get_board()
    # Remove the appropriate number of cells
    sudoku.remove_cells()
    # Get the final board after cells removal
    board = sudoku.get_board()
    # Return the representative 2D Python list of the board
    return board
