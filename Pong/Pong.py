# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:40:17 2017

@author: rjr
"""

import pygame, sys
from pygame.locals import *

# Number of FPS
FPS = 200

#Global variables
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

#Main function
def main():
    pygame.init()
    global DISPLAYSURF
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Pong")
    
    # Main game loop
    while True:     
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
if __name__=='__main__':
    main()
    