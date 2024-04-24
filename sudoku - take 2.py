# Consolidating sudoku.py and GUI.py into one.... - Nick

import pygame
import sys
from sudoku_generator import *
from cell2 import *
from grid import *

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

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Font for button text
font = pygame.font.Font(None, 36)

# Main menu loop
def main_menu():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(mouse_pos):
                    return "Easy"
                elif medium_button.collidepoint(mouse_pos):
                    return "Medium"
                elif hard_button.collidepoint(mouse_pos):
                    return "Hard"
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Draw buttons
        pygame.draw.rect(screen, BUTTON_COLOR, easy_button)
        pygame.draw.rect(screen, BUTTON_COLOR, medium_button)
        pygame.draw.rect(screen, BUTTON_COLOR, hard_button)
        
        # Draw button hover effect
        if easy_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, easy_button)
        elif medium_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, medium_button)
        elif hard_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, hard_button)
        
        # Add text to buttons
        easy_text = font.render("Easy", True, BUTTON_TEXT_COLOR)
        medium_text = font.render("Medium", True, BUTTON_TEXT_COLOR)
        hard_text = font.render("Hard", True, BUTTON_TEXT_COLOR)
        screen.blit(easy_text, (easy_button.x + 55, easy_button.y + 15))
        screen.blit(medium_text, (medium_button.x + 35, medium_button.y + 15))
        screen.blit(hard_text, (hard_button.x + 40, hard_button.y + 15))
        
        # Add LEVEL text
        level_text = font.render("LEVEL", True, BLACK)
        screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 50))
        
        # Update the display
        pygame.display.flip()

# Define button dimensions and positions
button_width = 150
button_height = 50
button_x = (SCREEN_WIDTH - button_width) // 2
easy_button = pygame.Rect(button_x, 150, button_width, button_height)
medium_button = pygame.Rect(button_x, 250, button_width, button_height)
hard_button = pygame.Rect(button_x, 350, button_width, button_height)

# Start the main menu loop
difficulty = main_menu()

# Generate Sudoku puzzle based on selected difficulty
if difficulty == "Easy":
    removed_cells = 30
elif difficulty == "Medium":
    removed_cells = 40
elif difficulty == "Hard":
    removed_cells = 50

sudoku = generate_sudoku(9, removed_cells)
#print(sudoku)  # For testing, print the generated Sudoku board

board = Board(9, 9, screen, difficulty)
board.draw()
#board.draw # test
#pygame.display.update()
pygame.display.flip()

