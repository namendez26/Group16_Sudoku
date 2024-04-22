import pygame
import sys
import os

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)
BUTTON_TEXT_COLOR = WHITE

# Define screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

class GUI:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sudoku Game")

        # Create buttons for Easy, Medium, and Hard modes
        button_width = 150
        button_height = 50
        button_x = (SCREEN_WIDTH - button_width) // 2
        self.easy_button = pygame.Rect(button_x, 150, button_width, button_height)
        self.medium_button = pygame.Rect(button_x, 250, button_width, button_height)
        self.hard_button = pygame.Rect(button_x, 350, button_width, button_height)

        # Font for button text
        self.font = pygame.font.Font(None, 36)

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy_button.collidepoint(event.pos):
                        #display board
                        pygame.quit()
                        sys.exit()
                    elif self.medium_button.collidepoint(event.pos):
                        #display board
                        pygame.quit()
                        sys.exit()
                    elif self.hard_button.collidepoint(event.pos):
                        #display board
                        pygame.quit()
                        sys.exit()
            # Clear the screen
            self.screen.fill(WHITE)

            # Draw buttons
            pygame.draw.rect(self.screen, BUTTON_COLOR, self.easy_button)
            pygame.draw.rect(self.screen, BUTTON_COLOR, self.medium_button)
            pygame.draw.rect(self.screen, BUTTON_COLOR, self.hard_button)


            if self.easy_button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, BUTTON_HOVER_COLOR, self.easy_button)
            elif self.medium_button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, BUTTON_HOVER_COLOR, self.medium_button)
            elif self.hard_button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, BUTTON_HOVER_COLOR, self.hard_button)

            # Add text to buttons
            easy_text = self.font.render("Easy", True, BUTTON_TEXT_COLOR)
            medium_text = self.font.render("Medium", True, BUTTON_TEXT_COLOR)
            hard_text = self.font.render("Hard", True, BUTTON_TEXT_COLOR)
            self.screen.blit(easy_text, (self.easy_button.x + 55, self.easy_button.y + 15))
            self.screen.blit(medium_text, (self.medium_button.x + 35, self.medium_button.y + 15))
            self.screen.blit(hard_text, (self.hard_button.x + 40, self.hard_button.y + 15))

            # Add LEVEL text
            level_text = self.font.render("LEVEL", True, BLACK)
            self.screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 50))

            # Update the display
            pygame.display.flip()

if __name__ == "__main__":
    gui = GUI()
    gui.loop()