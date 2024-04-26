import pygame
from cell import *

pygame.init()

# Properties #
LINE_COLOR = (0, 0, 0) # Black
THICKNESS_OUTER = 7
THICKNESS_INNER = 1
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)

class Board:
    def __init__(self, width, height, screen, difficulty, sudoku):
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard.
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(sudoku[row][col], row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None
        self.font = pygame.font.Font(None, 36)  # Font for displaying text
        self.buttons = {
            "Reset": pygame.Rect(650/3 - 140, 550, 100, 50),
            "Restart": pygame.Rect(650/3, 550, 100, 50),
            "Exit": pygame.Rect(650/3 + 140, 550, 100, 50)
        }

    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        
        # Clear the screen
        #self.screen.fill((255, 255, 255))
        background_image = pygame.image.load("matrix.jpg")
        #screen.fill(GRAY)
        self.screen.blit(background_image, (0, 0))
 
        
        # Draw Sudoku grid
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.draw(self.screen)
        
        for i in range(10):
            thickness = THICKNESS_OUTER if i % 3 == 0 else THICKNESS_INNER # Outline of 3x3 grid
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * (540/9)), (540, i * (540/9)), thickness)
            pygame.draw.line(self.screen, LINE_COLOR, (i * (540/9), 0), (i * (540/9), 540), thickness)  

        # Draw buttons below the board
        for btn_name, rect in self.buttons.items():
            # Draw button with hover effect if mouse is over it
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, BUTTON_HOVER_COLOR, rect)
            else:
                pygame.draw.rect(self.screen, BUTTON_COLOR, rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)  # Draw button outline
            text_surface = self.font.render(btn_name, True, (0, 0, 0))  # Render button text
            text_rect = text_surface.get_rect(center=rect.center)  # Center button text
            self.screen.blit(text_surface, text_rect)  # Draw button text

    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the currently selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.

        # Deselect previously selected cell
        if self.selected_cell:
            previous_row, previous_col = self.selected_cell
            self.cells[previous_row][previous_col].selected = False
        
        # Mark the newly selected cell
        self.selected_cell = (row, col)
        self.cells[row][col].selected = True

    def click(self, x, y):
        # If a tuple of (x, y) coordinates is within the displayed board,
        # this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None.
        
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].rect.collidepoint(x, y):
                    return row, col
        return None

    def clear(self):
        # Clears the value cell.
        # Note that the user can only remove the cell values and sketched value that are filled by themselves.
        
        if self.selected_cell:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            if not cell.is_given:
                cell.set_value(0)

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        
        if self.selected_cell:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            if not cell.is_given:
                cell.set_sketched_value(value)

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        if self.selected_cell:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            if not cell.is_given:
                cell.set_cell_value(value)

    def reset_to_original(self):
        # Reset all cells in the board to their original values
        # (0 if cleared, otherwise the corresponding digit).
        for row in range(9): # Iterates through rows 0-8
            for col in range(9): # Iterates through cols 0-8
                cell = self.cells[row][col] # cell in matrix [0-8][0-8]
                if not cell.is_given: # if cell wasn't provided at beginning,
                    cell.set_cell_value(0) # Return its value to zero...
                    cell.set_sketched_value(None) # and remove sketched values, too.

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        for row in range(9):
            for col in range(9):
                self.cells[row][col].update()

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        # Check whether the Sudoku board has unique numbers in each row and column.
        for row in range(9):
            for col in range(9):
                if not self.is_valid(row, col, self.cells[row][col].value):
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num))

    def valid_in_row(self, row, num):
        # Check if the number is unique in its row.
        return [cell.value for cell in self.cells[row]].count(num) == 1

    def valid_in_col(self, col, num):
        # Check if the number is unique in its column.
        return [self.cells[row][col].value for row in range(9)].count(num) == 1
