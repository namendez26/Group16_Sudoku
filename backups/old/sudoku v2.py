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
SCREEN_WIDTH = 630
SCREEN_HEIGHT = 630

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("(-: Group 16's Sudoku :-)")

# Font for button text
font = pygame.font.Font(None, 36)

# Main menu loop
def main_menu():
    menu = True
    
    while menu:
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
        screen.blit(easy_text, (easy_button.x, easy_button.y + 15))
        screen.blit(medium_text, (medium_button.x, medium_button.y + 15))
        screen.blit(hard_text, (hard_button.x, hard_button.y + 15))
        
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

# TODO: THIS IS TO DEBUG END SCREEN!!!
sudoku = generate_sudoku(9, 1)#removed_cells)
board = Board(9, 9, screen, difficulty, sudoku)


def endgame():
    screen.fill(WHITE) # New screen!
    if board.check_board(): # If user correctly solves board....
        you_won = font.render("Game Won!", True, BLACK)
        screen.blit(you_won, (SCREEN_WIDTH // 2 - you_won.get_width() // 2, 50))
        # Properties for Exit Button #
        exit_button_end = pygame.Rect(button_x, 350, button_width, button_height)
        pygame.draw.rect(screen, BUTTON_COLOR, exit_button_end)
        pygame.draw.rect(screen, BLACK, exit_button_end, 2)  # Button outline
        exit_text_end = font.render("Exit", True, BUTTON_TEXT_COLOR)
        screen.blit(exit_text_end, (exit_button_end.x + 10, exit_button_end.y + 15))

    else:
        you_lost = font.render("Game Over :(", True, BLACK)
        screen.blit(you_lost, (SCREEN_WIDTH // 2 - you_lost.get_width() // 2, 50))
        # Properties for Exit Button #
        restart_button_end = pygame.Rect(button_x, 350, button_width, button_height)
        pygame.draw.rect(screen, BUTTON_COLOR, restart_button_end)
        pygame.draw.rect(screen, BLACK, restart_button_end, 2)  # Button outline
        restart_text_end = font.render("Restart", True, BUTTON_TEXT_COLOR)
        screen.blit(restart_text_end, (restart_button_end.x + 10, restart_button_end.y + 15))
    pygame.display.flip()
    #return False

# Loop for Game in Progress
game_in_progress = True
while game_in_progress:

    if board.is_full():
        endgame()
        #game_in_progress = endgame()
        #game_in_progress = False # exits immediately, so don't use

    # The fun stuff #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_in_progress = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos
            clicked_cell = board.click(x, y)
            if clicked_cell:
                row, col = clicked_cell
                board.select(row, col)
            # Checks for user clicking bottom buttons.
            for btn_name, rect in board.buttons.items():
                if btn_name == "Reset" and rect.collidepoint(pos): # if user clicks "Reset"...
                    board.reset_to_original() # Board
                # I don't like how this very part turned out, but it works....
                if btn_name == "Restart" and rect.collidepoint(pos): # if user clicks "Restart"...        
                    # Clear the screen
                    screen.fill(WHITE)
                    # Show the main menu again to select difficulty
                    difficulty = main_menu()
                    # Generate Sudoku puzzle based on selected difficulty
                    if difficulty == "Easy":
                        removed_cells = 30
                    elif difficulty == "Medium":
                        removed_cells = 40
                    elif difficulty == "Hard":
                        removed_cells = 50
   
                    sudoku = generate_sudoku(9, removed_cells)
                    # Create a new board
                    board = Board(9, 9, screen, difficulty, sudoku)
 
                if btn_name == "Exit" and rect.collidepoint(pos): # if user clicks "Exit"...
                    pygame.quit()
        elif event.type == pygame.KEYDOWN: # If any key is pressed down
            if board.selected_cell: # While/if a cell is selected
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # If pressing return
                    # Submit guess
                    row, col = board.selected_cell # x, y
                    cell = board.cells[row][col] # cell in x-y matrix
                    sketched_value = cell.sketched_value
                    if sketched_value is not None:
                        board.place_number(sketched_value)
                elif event.key == pygame.K_LEFT:
                    # Move left
                    row, col = board.selected_cell
                    if col > 0:
                        board.select(row, col - 1)
                elif event.key == pygame.K_RIGHT:
                    # Move right
                    row, col = board.selected_cell
                    if col < board.width - 1:
                        board.select(row, col + 1)
                elif event.key == pygame.K_UP:
                    # Move up
                    row, col = board.selected_cell
                    if row > 0:
                        board.select(row - 1, col)
                elif event.key == pygame.K_DOWN:
                    # Move down
                    row, col = board.selected_cell
                    if row < board.height - 1:
                        board.select(row + 1, col)
                elif pygame.K_1 <= event.key <= pygame.K_9: # For normal 1-9 usage.
                    # Sketch number
                    sketched_value = event.key - pygame.K_0
                    row, col = board.selected_cell
                    board.sketch(sketched_value)
                elif pygame.K_KP1 <= event.key <= pygame.K_KP9: # For keypad 1-9 usage!
                    # Sketch number
                    sketched_value = event.key - pygame.K_KP0
                    row, col = board.selected_cell
                    board.sketch(sketched_value)
                elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    # Delete sketched value or user-entered value (excluding initial given values)
                    row, col = board.selected_cell
                    cell = board.cells[row][col]
                    if not cell.is_given:
                        cell.set_cell_value(0)
                        cell.set_sketched_value(None)
            elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                # Clear the entire board of sketched values and user-entered values
                for row in range(board.height):
                    for col in range(board.width):
                        cell = board.cells[row][col]
                        if not cell.is_given:
                            cell.set_cell_value(0)
                            cell.set_sketched_value(None)

        # Update the underlying 2D board with the values in all cells
        board.update_board()

        # Clear the screen
        screen.fill(WHITE)

        # Draw the board
        board.draw()

        # Update the display
        pygame.display.flip()

# Quit Pygame when the main loop exits
#pygame.quit()
