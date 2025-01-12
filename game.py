# Pac-Man clone made for learning/teaching git and Python

import random
import time
import pygame as pg

from pacman import PacMan
from ghost import Ghost
from level import Level

## Setup ##
pg.init()
width = 610 #8*32
height = 675 #7*32
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Pac-Man (clone)")

font_press_enter = pg.font.Font(None, 32)

## Game loop ##
state = "LOAD"
running = True
while running:
    
    if state == "LOAD":
        screen.fill((0,0,0)) 
        pacman = PacMan(1,1)
        ghost = Ghost(3,2)
        #ghost2 = Ghost(5,2)
        direction = None
        level = Level("level.txt")
        state = "READY"


    elif state == "READY":
        text = font_press_enter.render("Press [Enter] to play", True, (220,220,10))
        text_rect = text.get_rect(center=(width/2, height/2)) 
        screen.blit(text, text_rect)

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    state = "PLAY"

        pg.display.flip()  
        time.sleep(0.1)
        

    elif state == "PLAY":

        ## Handle events (keypresses etc.)
        events = pg.event.get()
        for event in events:

            # Close window (e.g. pressing [x] or Ctrl+F4)
            if event.type == pg.QUIT:
                running = False
            # Keypresses
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    direction = "up"
                elif event.key == pg.K_DOWN:
                    direction = "down"
                elif event.key == pg.K_LEFT:
                    direction = "left"
                elif event.key == pg.K_RIGHT:
                    direction = "right"
                elif event.key == pg.K_ESCAPE:
                    running = False


        ## Move / logic ##
        pacman.move(level,direction)
        ghost.move(level, pacman.row, pacman.col)



        ## Draw ##
        screen.fill((0,0,0)) 
        level.draw(screen, pacman)
        ghost.draw(screen)
        #ghost2.draw(screen)
        pacman.draw(screen, direction, ghost.row, ghost.col, state)

        # Update window with newly drawn pixels
        pg.display.flip()  

        # Limit framerate by waiting a 10-100 milliseconds
        state = pacman.state
        time.sleep(0.05)