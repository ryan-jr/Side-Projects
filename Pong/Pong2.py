# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 02:16:14 2018

@author: rjr
"""


# https://www.youtube.com/watch?v=gykTkxzku3Y

import pygame, sys
from pygame.locals import *
import random



pygame.init()
pygame.font.init()

width = 640
height = width / 16 * 9 # 360
FPS = 30
timer = pygame.time.Clock()
screen = pygame.display.set_mode((width, int(height)))
keys = [None] * 275
font = pygame.font.Font("origa___.ttf", 15)


# Player paddles
paddleSpeed = 5
paddleMargin = 50
paddleWidth = 25
paddleHeight = 100

paddle1 = {"x":paddleMargin, "y":50, "score":0}
paddle2 = {"x":(width - (paddleWidth + paddleMargin)), "y":50, "score":0}




# ball
ballXSpeed = 5
ballYSpeed = 5
ballDir = [-5, 5]
ball = {"x":random.randint(0, width), "y":random.randint(0, height), "radius":16}


BLACK = (0,0,0)
WHITE = (255,255,255)



while True:
    screen.fill(BLACK)
    timer.tick(FPS)
    scoreText = font.render(str(paddle1["score"]) + " " + str(paddle2["score"]), False, WHITE)
    
    # Paddle 1
    pygame.draw.rect(screen, WHITE, (paddle1["x"], paddle1["y"], paddleWidth, paddleHeight))

    # Paddle 2
    pygame.draw.rect(screen, WHITE, (paddle2["x"], paddle2["y"], paddleWidth, paddleHeight))
    
    # ball
    pygame.draw.circle(screen, WHITE, (int(ball["x"]), int(ball["y"])), ball["radius"])
    
    # Render score
    screen.blit(scoreText, (width / 2, 10))
    
    # Edge detection
    if (ball["x"]) - (ball["radius"]) <= 0:
        ball["x"] = width / 2
        ball["y"] = height / 2
        ballXSpeed = ballDir[random.randint(0, 1)]
        paddle2["score"] += 1
    elif (ball["x"]) + (ball["radius"]) >= width:
        ball["x"] = width / 2
        ball["y"] = height / 2
        ballXSpeed = ballDir[random.randint(0, 1)]
        paddle1["score"] += 1
        
    if (ball["y"]) - (ball["radius"]) <= 0:
        ballYSpeed = 5
    elif (ball["y"]) + (ball["radius"]) >= height:
        ballYSpeed = -5
        
    # Paddle detection
    if ball["x"] <= (paddle1["x"] + paddleWidth) and (ball["y"] >= paddle1["y"] and ball["y"] <= (paddle1["y"] + paddleHeight)):
        print("Collision")
        ballXSpeed = 5
    if ball["x"] >= paddle2["x"] and ball["y"] >= paddle2["y"] and ball["y"] <= (paddle2["y"] + paddleHeight):
        print("Collision")
        ballXSpeed = -5
        
        
    ball["x"] += ballXSpeed
    ball["y"] += ballXSpeed
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit(0)
        elif event.type == KEYDOWN:
            print(event.key)
            keys[event.key] = True
        elif event.type == KEYUP:
            print(event.key)
            keys[event.key] = False
            
        
            
    # Player controls
    # Player 1
    if keys[K_w] and paddle1["y"] > 0:
        paddle1["y"] -= paddleSpeed
    elif keys[K_s] and (paddle1["y"] + paddleHeight) < height:
        paddle1["y"] += paddleSpeed
        
    # Player 2
    if keys[K_UP] and paddle2["y"] > 0:
        paddle2["y"] -= paddleSpeed
    elif keys[K_DOWN] and (paddle2["y"] + paddleHeight) < height:
        paddle2["y"] += paddleSpeed
        
    # End player controls
        
                
    
    pygame.display.update()
    