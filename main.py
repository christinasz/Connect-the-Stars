import pygame, sys, pyganim
from pygame.locals import *
from player import *
from const import *

#set up pygame
pygame.init()
fpsClock = pygame.time.Clock()

# window
windowSurface = pygame.display.set_mode((1280, 720), 0, 32)

Player = Player()

# set up fonts
defaultFont = pygame.font.SysFont('gotham.ttf', 60)

title = defaultFont.render('Connect the Stars', True, WHITE)
titleRect = title.get_rect()
titleRect.centerx = windowSurface.get_rect().centerx
titleRect.centery = windowSurface.get_rect().centery

play = defaultFont.render('Play', True, WHITE)

pygame.display.update()

# GAME LOOP
while 1:
    windowSurface.fill(WHITE)
    windowSurface.blit(title, titleRect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # PLAYER MOVEMENT
    key = pygame.key.get_pressed()

    # jumping
    if key[pygame.K_UP] or key[pygame.K_SPACE]:
        Player.jumping = True
        Player.update('jump')

    # moving right
    if key[pygame.K_RIGHT]: 
        Player.update('right')

    # moving left
    elif key[ pygame.K_LEFT]: 
        Player.update('left')

    #idle
    else: Player.update('idle')
    
    Player.image.blit(windowSurface, (Player.x, Player.y))
                                    
    pygame.display.update()
    fpsClock.tick(FPS)


