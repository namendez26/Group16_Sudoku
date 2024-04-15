from cell import Cell
import pygame

WIDTH = 550

BG_COLOR = (255, 255, 245)

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.cells = [[Cell(0, row, col, screen) for col in range(1, 10)] for row in range(1, 10)]
        self.difficulty = difficulty

    def draw(self):
        window = pygame.display.set_mode((WIDTH, WIDTH))     #create window for the game
        pygame.display.set_caption("Welcome to Sudoku")
        window.fill(BG_COLOR)
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (i * 50 + 50, 50), (i * 50+50, 500), 4)
                pygame.draw.line(self.screen, (0, 0, 0), (0, 50 + 50*i), (500, 50+50*i), 4)
            else:
                pygame.draw.line(self.screen, (0, 0, 0), (i * 50 + 50, 50), (i * 50 + 50, 500), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (0, 50 + 50 * i), (500, 50 + 50 * i), 2)

        pygame.display.update()


    def select(self, row, col):
        for r in range(1,10):
            for c in range(1,10):
                self.cells[r-1][c-1].selected = False
        self.cells[row-1][col-1].selected = True

    def click(self, x, y):
        cell_size = self.width // 9
        col = x // cell_size
        row = y // cell_size
        if col <= 9 and row <= 9:
            return [row + 1, col + 1]
        else:
            return None

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
