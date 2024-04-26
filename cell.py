import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        # Constructor for the Cell class #
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.rect = pygame.Rect(col * (540/9), row * (540/9), 540/9, 540/9)
        self.is_given = True if value != 0 else False
        self.font = pygame.font.Font(None, 36)  # Font for displaying text
        self.sketched_value = None  # Initialize sketched_value attribute to None
        self.selected = False

    def set_cell_value(self, value):
        # Setter for this cell’s value #
        self.value = value

    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value #
        self.sketched_value = value

    def draw(self, screen):
                # Draws this cell, along with the value inside it.
                # If this cell has a nonzero value, that value is displayed.
                # Otherwise, no value is displayed in the cell.
                # The cell is outlined green if it is currently selected.
                if self.selected:
                    pygame.draw.rect(screen, (0, 200, 0), self.rect, 4)  # Draw green outline if selected
                else:
                    pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)  # Draw cell outline
                    pygame.draw.rect(screen, (100, 100, 100), self.rect)  # Draw cell outline
                if self.value != 0:
                    text_surface = self.font.render(str(self.value), True, (255, 255, 255))  # Render cell value
                    screen.blit(text_surface, (self.rect.x + 20, self.rect.y + 15))  # Draw cell value
                else:
                    if self.sketched_value is not None:
                        # Render sketched value if exists
                        #sketched_text_surface = self.font.render(str(self.sketched_value), True, (128, 128, 128)) # Sketches value in grey
                        sketched_text_surface = self.font.render(str(self.sketched_value), True, (0, 200, 0)) # Sketches value in green
                        screen.blit(sketched_text_surface, (self.rect.x + 5, self.rect.y + 5))

    def update(self):
        pass  # Update cell appearance if needed
