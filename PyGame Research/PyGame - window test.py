import pygame

'''
https://www.youtube.com/watch?v=y9VG3Pztok8
'''

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = pygame.Rect((300,250,50,50))

sudoku = True
while sudoku:
    
    pygame.draw.Rect(screen,(255,0,0),player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sudoku = False

pygame.QUIT()