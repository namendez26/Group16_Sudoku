import pygame
import sys
import random

# Function to check if placing a number in a cell is valid
def is_valid_move(grid, row, col, num):
    # Check if the same number exists in the row
    if num in grid[row]:
        return False

    # Check if the same number exists in the column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if the same number exists in the 3x3 subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if grid[i][j] == num:
                return False

    return True

# Function to recursively solve the Sudoku puzzle
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Check if the cell is empty
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_valid_move(grid, row, col, num):  # Check if the number is valid
                        grid[row][col] = num  # Place the number in the cell
                        if solve_sudoku(grid):  # Recursively solve the next cell
                            return True
                        grid[row][col] = 0  # Backtrack if the number doesn't lead to a solution
                return False
    return True  # Return True if the puzzle is solved

# Function to generate a complete Sudoku grid
def generate_complete_sudoku(grid):
    # Start with an empty grid
    for row in range(9):
        for col in range(9):
            grid[row][col] = 0

    # Generate a complete Sudoku grid
    solve_sudoku(grid)

# Example usage:
grid = [[0 for _ in range(9)] for _ in range(9)]  # Create an empty grid
generate_complete_sudoku(grid)  # Generate a complete Sudoku grid
print(grid)  # Print the generated grid

'''
Everything above here is 
    1) scrambling the grid;
    2) varying the number of blanks (0s) based on difficulty:
        - 30 if difficulty == Easy
        - 40 if difficulty == Medium
        - 50 if difficulty == Hard
        
Everything below here is the original code.
'''

# Initialize Pygame
pygame.init()

# Set up the display window
WIDTH, HEIGHT = 540, 540
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku") # window name

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GATOR_BLUE = (0, 33, 165)
GATOR_ORANGE = (250, 70, 22)

# Define the Sudoku grid (0 represents empty cell)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to draw the Sudoku grid
def draw_grid():
    for i in range(10): # Up to 9
        if i % 3 == 0:
            thickness = 10 # Dividing border between 3x3
        else:
            thickness = 1 # Normal borders
        pygame.draw.line(WINDOW, GATOR_BLUE, (0, i * HEIGHT // 9), (WIDTH, i * HEIGHT // 9), thickness) # Horizontal draw
        pygame.draw.line(WINDOW, GATOR_BLUE, (i * WIDTH // 9, 0), (i * WIDTH // 9, HEIGHT), thickness) # Vertical draw

# Function to draw the numbers on the Sudoku grid
def draw_numbers():
    font = pygame.font.Font(None, 40)  # Set the font to None (default system font) with a size of 40
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:  # Check if the cell is not empty
                # Render the number as text using the chosen font and color (GATOR_BLUE)
                text = font.render(str(grid[i][j]), True, GATOR_ORANGE)
                # Get the rectangle that encloses the rendered text and center it on the cell
                text_rect = text.get_rect(center=(j * WIDTH // 9 + WIDTH // 18, i * HEIGHT // 9 + HEIGHT // 18))
                # Blit (draw) the rendered text onto the window at the calculated position
                WINDOW.blit(text, text_rect)

# Main loop
running = True  # Variable to control the main loop
while running:  # Continue looping as long as the variable 'running' is True
    WINDOW.fill(WHITE)  # Fill the window with white color
    draw_grid()  # Draw the Sudoku grid
    draw_numbers()  # Draw the numbers on the Sudoku grid
    for event in pygame.event.get():  # Iterate over each event in the event queue
        if event.type == pygame.QUIT:  # Check if the event is a quit event (user closing the window)
            running = False  # Set the 'running' variable to False to exit the loop and quit the program
    pygame.display.flip()  # Update the display to show the changes made in this iteration

pygame.quit()
sys.exit()