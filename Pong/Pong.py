# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:40:17 2017

@author: rjr
"""

import pygame, sys
from pygame.locals import *

# Number of FPS
FPS = 200

# Global variables
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

# Setting up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Draws the game arena
def drawArena():
    DISPLAYSURF.fill((0,0,0))
    # Draw outline of arena
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
    
    # Draw center line
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT), (LINETHICKNESS/4))

# Draws the paddle
def drawPaddle(paddle):
    # Stops paddle from moving too low/too high
    
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
        
    # Draws paddle
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)
        
# Draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)

# Moves the ball returns new position
def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball
    


# Main function
def main():
    pygame.init()
    global DISPLAYSURF
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Pong")
    
    
    #Initiate variable and set starting positions
    #any future changes made within rectangles
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) /2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) /2
    
                        
    #Creates Rectangles for ball and paddles.
    paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition, LINETHICKNESS,PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS,PADDLESIZE)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)
    
    
    # Draws the starting position of the Arena
    #drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)
    
    
    # Main game loop
    while True:     
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
          
       #drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)
       
# TODO: ball and drawArena() are breaking things...find out why
        ball = moveBall(ball, ballDirX, ballDirY)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
if __name__=='__main__':
    main()
    