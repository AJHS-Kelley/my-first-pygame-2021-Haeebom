# My First PyGame, Naomi Williams, 11/29/21 2:28 pm, v0.1

import pygame, sys
from pygame.locals import *

# Start Pygame
pygame.init()

# Setup our window. 1
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_mode('Hello, world!')

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)