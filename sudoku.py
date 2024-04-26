import pygame
import sys
from sudoku_generator import *
from cell import *
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

# Define button dimensions and positions
button_width = 150
button_height = 50
button_x = (SCREEN_WIDTH - button_width) // 2
easy_button = pygame.Rect(button_x, 150, button_width, button_height)
medium_button = pygame.Rect(button_x, 250, button_width, button_height)
hard_button = pygame.Rect(button_x, 350, button_width, button_height)
debug_button = pygame.Rect(button_x, 450, button_width, button_height)

def main_menu():
    menu = True
    while menu:
        
        # Clear the screen
        #screen.fill(WHITE)
        background_image = pygame.image.load("matrix.jpg")
        #screen.fill(GRAY)
        screen.blit(background_image, (0, 0))
         
        # Draw buttons
        pygame.draw.rect(screen, BUTTON_COLOR, easy_button)
        pygame.draw.rect(screen, BUTTON_COLOR, medium_button)
        pygame.draw.rect(screen, BUTTON_COLOR, hard_button)
        pygame.draw.rect(screen, BUTTON_COLOR, debug_button)
        
        # Draw button hover effect
        if easy_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, easy_button)
        elif medium_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, medium_button)
        elif hard_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, hard_button)

        elif debug_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, debug_button)
         
        # Add text to buttons
        easy_text = font.render("Easy", True, BUTTON_TEXT_COLOR)
        medium_text = font.render("Medium", True, BUTTON_TEXT_COLOR)
        hard_text = font.render("Hard", True, BUTTON_TEXT_COLOR)
        debug_text = font.render("Debug", True, BUTTON_TEXT_COLOR)

        # center the text
        easycenter = easy_text.get_rect(center=easy_button.center)
        mediumcenter = medium_text.get_rect(center=medium_button.center)
        hardcenter = hard_text.get_rect(center=hard_button.center)
        debugcenter = debug_text.get_rect(center=debug_button.center)

        screen.blit(easy_text, easycenter)
        screen.blit(medium_text, mediumcenter)
        screen.blit(hard_text, hardcenter)
        screen.blit(debug_text, debugcenter)
        
        # Add LEVEL text
        level_text1 = font.render("Welcome to the MATRIX.", True, WHITE)
        level_text2 = font.render("Choose a difficulty:", True, WHITE)
        screen.blit(level_text1, (SCREEN_WIDTH // 2 - level_text1.get_width() // 2, 40))
        screen.blit(level_text2, (SCREEN_WIDTH // 2 - level_text2.get_width() // 2, 90))
        
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
                        elif debug_button.collidepoint(mouse_pos):
                            return "Debug"


        # Update the display
        pygame.display.flip()

def game_end(board):
    while True:  # Loop until restart flag is True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if board.check_board():
                    if end_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                else:
                    if end_button.collidepoint(pygame.mouse.get_pos()):
                        main()

        # Draw the game over screen
        #screen.fill(WHITE)  # New screen!
        background_image = pygame.image.load("matrix.jpg")
        #screen.fill(GRAY)
        screen.blit(background_image, (0, 0))
         
        end_button = pygame.Rect(button_x, 350, button_width, button_height)
        pygame.draw.rect(screen, BUTTON_COLOR, end_button)
        # BLACK TO WHITE
        pygame.draw.rect(screen, WHITE, end_button, 2)  # Button outline
        
        if board.check_board():  # If user correctly solves the board
            end_text = font.render("Game Won!", True, WHITE)
            end_button_text = font.render("Exit", True, BUTTON_TEXT_COLOR)
        else:
            end_text = font.render("Game Over :(", True, WHITE)
            end_button_text = font.render("Restart", True, BUTTON_TEXT_COLOR)
        
        screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, 50))
        screen.blit(end_button_text, (end_button.x + 10, end_button.y + 15))
        
        pygame.display.flip()

def main():

    # Start the main menu loop
    difficulty = main_menu()

    # Generate Sudoku puzzle based on selected difficulty
    if difficulty == "Easy":
        removed_cells = 30
    elif difficulty == "Medium":
        removed_cells = 40
    elif difficulty == "Hard":
        removed_cells = 50
    elif difficulty == "Debug":
        removed_cells = 1


    # Generate Sudoku puzzle
    sudoku = generate_sudoku(9, removed_cells)
    board = Board(9, 9, screen, difficulty, sudoku)

    # Loop for Game in Progress
    game = True
    
    while game:
        if board.is_full():
            game = False
            # Call game_end() with the board object passed as argument
            if game_end(board):  
                # Reset the game state by reinitializing the board with the selected difficulty
                # Generate Sudoku puzzle
                sudoku = generate_sudoku(9, removed_cells)
                board = Board(9, 9, screen, difficulty, sudoku)

        # The fun stuff #
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                selected_cell = board.click(x, y)
                
                if selected_cell:
                    row, col = selected_cell
                    board.select(row, col)
                
                # Checks for user clicking bottom buttons.
                for btn_name, rect in board.buttons.items():
                    if btn_name == "Reset" and rect.collidepoint(pos):  # if user clicks "Reset"...
                        board.reset_to_original()  # Board
                    elif btn_name == "Restart" and rect.collidepoint(pos):  # if user clicks "Restart"...
                        # Clear the screen
                        #screen.fill(WHITE)
                        background_image = pygame.image.load("matrix.jpg")
                        #screen.fill(GRAY)
                        screen.blit(background_image, (0, 0))
         
                        # Show the main menu again to select difficulty [running main() again]
                        main()
                    elif btn_name == "Exit" and rect.collidepoint(pos):  # if user clicks "Exit"...
                        pygame.quit()
            
            elif event.type == pygame.KEYDOWN:  # If any key is pressed down
                
                if board.selected_cell:  # While/if a cell is selected
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:  # If pressing return
                        # Submit guess
                        row, col = board.selected_cell  # Get selected cell coordinates (x, y)
                        cell = board.cells[row][col]  # Access the selected cell in the board
                        sketched_value = cell.sketched_value  # Get the sketched value in the cell
                        if sketched_value is not None:
                            board.place_number(sketched_value)  # Place the sketched number in the cell
                    
                    # Arrow movement among grid (can be consolidated, but oh well...)
                    elif event.key == pygame.K_LEFT:  # If pressing left arrow key
                        # Move left
                        row, col = board.selected_cell  # Get selected cell coordinates (x, y)
                        if col > 0:
                            board.select(row, col - 1)  # Select the cell to the left
                    elif event.key == pygame.K_RIGHT:  # If pressing right arrow key
                        # Move right
                        row, col = board.selected_cell  # Get selected cell coordinates (x, y)
                        if col < board.width - 1:
                            board.select(row, col + 1)  # Select the cell to the right
                    elif event.key == pygame.K_UP:  # If pressing up arrow key
                        # Move up
                        row, col = board.selected_cell  # Get selected cell coordinates (x, y)
                        if row > 0:
                            board.select(row - 1, col)  # Select the cell above
                    elif event.key == pygame.K_DOWN:  # If pressing down arrow key
                        # Move down
                        row, col = board.selected_cell  # Get selected cell coordinates (x, y)
                        if row < board.height - 1:
                            board.select(row + 1, col)  # Select the cell below
                    
                    elif pygame.K_1 <= event.key <= pygame.K_9 or pygame.K_KP1 <= event.key <= pygame.K_KP9:  # For both normal and keypad 1-9 key usage
                        # Sketch number
                        if pygame.K_1 <= event.key <= pygame.K_9:
                            sketched_value = event.key - pygame.K_0  # Convert key code to integer value for normal keys
                        else:
                            sketched_value = event.key - pygame.K_KP0  # Convert key code to integer value for keypad keys
                        row, col = board.selected_cell  # Get selected cell coordinates (x, y)
                        board.sketch(sketched_value)  # Sketch the number in the cell

                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:  # If pressing delete or backspace
                        # Delete sketched value or user-entered value (excluding initial given values)
                        row, col = board.selected_cell  # Get selected cell coordinates (x, y)
                        cell = board.cells[row][col]  # Access the selected cell in the board
                        if not cell.is_given:  # Check if cell value is not given initially
                            cell.set_cell_value(0)  # Reset cell value to 0
                            cell.set_sketched_value(None)  # Clear sketched value for the cell
                else:  # If no cell is selected
                    if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:  # If pressing delete or backspace
                        # Clear the entire board of sketched values and user-entered values
                        for row in range(board.height):  # Iterate over each row
                            for col in range(board.width):  # Iterate over each column
                                cell = board.cells[row][col]  # Access the cell in the board
                                if not cell.is_given:  # Check if cell value is not given initially
                                    cell.set_cell_value(0)  # Reset cell value to 0
                                    cell.set_sketched_value(None)  # Clear sketched value for the cell

            # Update the underlying 2D board with the values in all cells
            board.update_board()
            # Clear the screen
            #screen.fill(WHITE)
            background_image = pygame.image.load("matrix.jpg")
            #screen.fill(GRAY)
            screen.blit(background_image, (0, 0))
         
            # Draw the board
            board.draw()
            # Update the display
            pygame.display.flip()
    # Quit Pygame when the main loop exits
    game_end(board)  # game_end screen should only show up when board_is.full() so make sure this doesn't happen when normally exiting....

# Start the main function
if __name__ == "__main__":
    main()
