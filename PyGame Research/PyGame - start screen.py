import pygame
import sys

pygame.init() # Initialize Pygame #

# Creating our game window #
WIDTH, HEIGHT = 550, 550
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Group 16 - Sudoku")

# Color Palette #
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GATOR_BLUE = (0, 33, 165)
GATOR_ORANGE = (250, 70, 22)

# Background Image #
background_image = pygame.image.load("sudoku_test_screen.jpg")

# Function to display text on the screen #
def display_text(text, font, size, color, x, y):

    font = pygame.font.Font(font, size) # Creation of font object with the specified font and size #
    text_surface = font.render(text, True, color) # Render text onto surface with the specified color #
    text_rect = text_surface.get_rect() # Get the rectangle that encloses the rendered text #
    text_rect.center = (x, y) # Set text rectangle's center coordinates #
    WINDOW.blit(text_surface, text_rect) # "Blit"/draw rendered text onto window at specified position #

# Main menu loop
def main_menu():
    
    running = True
    
    while running:
       
        # First layer = background color
        WINDOW.fill(WHITE)
        
        # Second layer image ATOP background color ~ consider the layers!
        WINDOW.blit(background_image, (0, 0))
        
        # Text
        display_text("Welcome", None, 54, GATOR_BLUE, (WIDTH / 3)*2+60, HEIGHT / 4)
        display_text("to", None, 54, GATOR_BLUE, (WIDTH / 3)*2+60, HEIGHT / 4 + 45)
        display_text("Sudoku!", None, 54, GATOR_BLUE, (WIDTH / 3)*2+60, HEIGHT / 4 + 90)
        display_text("Select Game Mode:", None, 42, BLACK, (WIDTH / 2), (HEIGHT / 3) * 2.2)

        # Create instances of DIFFICULTY
        easy_button = pygame.Rect((WIDTH / 4) - 60, HEIGHT / 2 + 180, 120, 50)
        medium_button = pygame.Rect(WIDTH / 2 - 60, HEIGHT / 2 + 180, 120, 50)
        hard_button = pygame.Rect(3 * (WIDTH / 4) - 60, HEIGHT / 2 + 180, 120, 50)
        
        # Draw buttons for DIFFICULTY
        pygame.draw.rect(WINDOW, GATOR_ORANGE, easy_button)
        pygame.draw.rect(WINDOW, GATOR_ORANGE, medium_button)
        pygame.draw.rect(WINDOW, GATOR_ORANGE, hard_button)
        
        # Insert text in DIFFICULTY buttons
        display_text("Easy", None, 36, WHITE, easy_button.centerx, easy_button.centery)
        display_text("Medium", None, 36, WHITE, medium_button.centerx, medium_button.centery)
        display_text("Hard", None, 36, WHITE, hard_button.centerx, hard_button.centery)

        # Updates screen (could use .update() method too, but .flip() is full-screen .update())
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():  # Constantly iterates over each event in the event queue
            
            if event.type == pygame.QUIT:  # Check event: if user closes window (QUIT event)
                running = False  # Set the 'running' variable to False, exiting loop and quiting program
            
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Check event: if user presses mouse (and isn't quitting)
                
                mouse_pos = pygame.mouse.get_pos()  # Get mouse's current position
                
                # Check within which button the mouse click's boundaries occurred
                if easy_button.collidepoint(mouse_pos): # collidepoint is boolean method, checking within rectangle's (x,y) boundaries
                    return "Easy"
                elif medium_button.collidepoint(mouse_pos):
                    return "Medium"
                elif hard_button.collidepoint(mouse_pos):
                    return "Hard"  # Return "Hard" to indicate the selected difficulty

difficulty = main_menu() # Game start screen
print("Select Game Mode:", difficulty) # Test for functionality! Yay, it works!

# Quits when user chooses difficulty #
pygame.quit()
sys.exit()