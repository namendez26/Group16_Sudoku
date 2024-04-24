import pygame
from cell2 import *

pygame.init()

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None
        self.font = pygame.font.Font(None, 36)  # Font for displaying text
        self.buttons = {
            "Reset": pygame.Rect(50, 550, 100, 50),
            "Restart": pygame.Rect(200, 550, 100, 50),
            "Exit": pygame.Rect(350, 550, 100, 50)
        }

    def draw(self):
        self.screen.fill((255, 255, 255))  # Clear the screen
        # Draw Sudoku grid
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.draw(self.screen)

        # Draw buttons below the board
        for btn_name, rect in self.buttons.items():
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)  # Draw button outline
            text_surface = self.font.render(btn_name, True, (0, 0, 0))  # Render button text
            self.screen.blit(text_surface, (rect.x + 10, rect.y + 10))  # Draw button text

    def select(self, row, col):
        self.selected_cell = (row, col)

    def click(self, x, y):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].rect.collidepoint(x, y):
                    return row, col
        return None

    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            if not cell.is_given:
                cell.set_value(0)

    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            if not cell.is_given:
                cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            if not cell.is_given:
                cell.set_value(value)

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                if not cell.is_given:
                    cell.set_value(0)

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].update()

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        for row in range(9):
            for col in range(9):
                if not self.is_valid(row, col, self.cells[row][col].value):
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))

    def valid_in_row(self, row, num):
        return num not in [cell.value for cell in self.cells[row]]

    def valid_in_col(self, col, num):
        return num not in [self.cells[row][col].value for row in range(9)]

    def valid_in_box(self, row_start, col_start, num):
        return num not in [self.cells[row][col].value for row in range(row_start, row_start + 3) for col in range(col_start, col_start + 3)]
