import sys
import pygame
from pygame.locals import *

def hello_world():
    pygame.init()
    pygame.display.set_mode((480 ,320))
    pygame.display.set_caption('Hello world!')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
if __name__ =='__main__':
    hello_world()
