# My First PyGame, Naomi Williams, 12/01/21 2:28 pm, v0.7

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
PURPLERAIN = (128, 110, 255)

# Setup font.
basicFont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill backgound color.
windowSurface.fill(PURPLERAIN)

# Draw a polygon onto the screen
pygame.draw.polygon(windowSurface, BLACK, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw lines on the screen.
pygame.draw.line(windowSurface, WHITE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (75, 60), (60, 75), 2)
pygame.draw.line(windowSurface, RED, (0, 150), (150, 0), 1)

# Draw a circle.
pygame.draw.circle(windowSurface, BLACK, (300, 50), 20, 0)

# Draw an ellipse.
pygame.draw.ellipse(windowSurface, RED,(300, 250, 40, 80), 1)

# Draw the text rectangle.
pygame.draw.rect(windowSurface, WHITE, (textRect.left - 20, textRect.width + 40, textRect.height + 40))

# Create Pixel Array
pixArray = pygame.pixelArray(windowSurface)
pixArray [480][380] = BLACK
del pixArray