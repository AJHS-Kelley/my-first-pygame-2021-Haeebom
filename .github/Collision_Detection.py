# Pygame Collision Detection Practice, Naomi Williams, Januaray 26, 2022, 11:43am, v0.2

import pygame, sys, random
from pygame.locals import *

# Setup Pygame
pygame.init()
mainClock = pygame.time.Clock()

# Setup The Pygame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection 2022')
