import pygame as pg
import random

class Ghost:

    def __init__(self, row, col):

        # https://sfxr.me/#34T6PktF8TcRjBGBCtaWAp8xrJeEmwSfouC2KVwAWC42iM2UWcDqruxhd8Xq4MFBc7kMaDGuyeyqde9ddiWDHprGh2dvs6Ery9NZQmbQM9gyXmSZzdhxPnMnw
        # https://sfxr.me/#34T6PkpqAUU8XZ3ze41FCou6ZCuAPdnvQEjkm2P1TPRMxjSRZdiQm9e5DJF1dPTvN8C3gPXJ7DuFniwZVHsmDC5qDkCUYDnkkgQAsqe9MaC2pHxKexVqdd5Jw
        self.sound_move0 = pg.mixer.Sound("sounds/pacman_move_0.wav")
        self.sound_move1 = pg.mixer.Sound("sounds/pacman_move_1.wav")
        self.sound_move0.set_volume(0.5)
        self.sound_move1.set_volume(0.5)

        self.col = col
        self.row = row

        self.images = []
        for i in range(2):
            img = pg.image.load(f"images/ghost_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0


    def move(self, level, pacr, pacc):
        #cor = random.randint(1,2)
        #movement = random.randint(-1,1)
        movement_col = 0
        movement_row = 0
        self.prev_mov = [0,0]
        if self.tick%2 == 1:
            if pacr > self.row:
                movement_row = 1
                if level.tiles[self.row+movement_row][self.col] != "#" and self.row+movement_row != self.prev_mov[0]:
                    self.prev_mov[0] = self.row
                    self.prev_mov[1] = self.col
                    self.row += movement_row
                elif level.tiles[self.row][self.col+1] != "#" and self.col+1 != self.prev_mov[1]:
                    self.prev_mov[0] = self.row
                    self.prev_mov[1] = self.col
                    self.col += 1
            
            elif pacr < self.row:
                movement_row = -1
                if level.tiles[self.row+movement_row][self.col] != "#":
                    self.row += movement_row
                elif level.tiles[self.row][self.col-1] != "#":
                    self.col -= 1

            elif pacc > self.col:
                movement_col = 1
                if level.tiles[self.row][self.col+movement_col] != "#":
                    self.col += movement_col
                elif level.tiles[self.row+1][self.col] != "#":
                    self.row += 1

            else:
                movement_col = -1
                if level.tiles[self.row][self.col+movement_col] != "#":
                    self.col += movement_col
                elif level.tiles[self.row-1][self.col] != "#":
                    self.row -= 1

        #if cor == 1:
            #if level.tiles[self.row][self.col+movement_col] != "#":
                #self.col += movement_col
            #elif level.tiles[self.row+movement_row][self.col] != "#":
                #self.row += movement_row
        #else:
            #if level.tiles[self.row+movement_row][self.col] != "#":
                #self.row += movement_row
            #elif level.tiles[self.row][self.col+movement_col] != "#":
                #self.col += movement_col

        self.tick += 1 
    
    def draw(self,screen):
        r = self.tick%2
        screen.blit(self.images[r], (self.col*32, self.row*32)) 