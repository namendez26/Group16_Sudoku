import pygame

'''
https://www.youtube.com/watch?v=y9VG3Pztok8
'''

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = pygame.Rect((300,250,50,50))

sudoku = True # Initializer
while sudoku:
    
    screen.fill((0,0,0)) # Background fill, leaving no trail.
    
    pygame.draw.rect(screen,(0,255,0),player) # Green square.
    
    # directional pad creator #
    key = pygame.key.get_pressed() # currently pressed key [to be moved in-place (x,y)]
    if key[pygame.K_a] == True: # if A
        player.move_ip(-1,0) # go left
    elif key[pygame.K_d] == True: # if D
        player.move_ip(1,0) # go right
    elif key[pygame.K_w] == True: # if W
        player.move_ip(0,-1) # go up
    elif key[pygame.K_s] == True: # if S
        player.move_ip(0,1) # go down

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sudoku = False
    
    pygame.display.update()

pygame.QUIT()