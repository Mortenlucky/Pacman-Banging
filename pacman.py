import pygame as pg

class PacMan:

    def __init__(self, row, col):

        # https://sfxr.me/#34T6PktF8TcRjBGBCtaWAp8xrJeEmwSfouC2KVwAWC42iM2UWcDqruxhd8Xq4MFBc7kMaDGuyeyqde9ddiWDHprGh2dvs6Ery9NZQmbQM9gyXmSZzdhxPnMnw
        # https://sfxr.me/#34T6PkpqAUU8XZ3ze41FCou6ZCuAPdnvQEjkm2P1TPRMxjSRZdiQm9e5DJF1dPTvN8C3gPXJ7DuFniwZVHsmDC5qDkCUYDnkkgQAsqe9MaC2pHxKexVqdd5Jw
        self.sound_move0 = pg.mixer.Sound("sounds/pacman_move_0.wav")
        self.sound_move1 = pg.mixer.Sound("sounds/pacman_move_1.wav")
        self.sound_move0.set_volume(0.5)
        self.sound_move1.set_volume(0.5)

        self.start = [row,col]
        self.col = col
        self.row = row
        self.point = 0
        self.direction = False

        self.images = []
        for i in range(6):
            img = pg.image.load(f"images/pacman_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0

    def move(self, level, direction):
        # Move pacman
        moving = False
        # self_row = self_x
        # self_col = self_y

        # Temp direction

        if direction == "up":
            if level.tiles[int(self.row-0.125)][int(self.col)] != "#" and self.col-int(self.col) == 0:
                self.direction = "up"
        if direction == "down":
            if level.tiles[int(self.row+1)][int(self.col)] != "#" and self.col-int(self.col) == 0:
                self.direction = "down"
        if direction == "left":
            if level.tiles[int(self.row)][int(self.col-0.125)] != "#" and self.row-int(self.row) == 0:
                self.direction = "left"
        if direction == "right":
            if level.tiles[int(self.row)][int(self.col+1)] != "#" and self.row-int(self.row) == 0:
                self.direction = "right"
        
        # Actual Direction

        if self.direction == "up":
            if level.tiles[int(self.row-0.125)][int(self.col)] != "#" and self.col-int(self.col) == 0:
                self.row -= 0.125
                moving = True
        elif self.direction == "down":
            if level.tiles[int(self.row+1)][int(self.col)] != "#" and self.col-int(self.col) == 0:
                self.row += 0.125
                moving = True
        elif self.direction == "left":
            if level.tiles[int(self.row)][int(self.col-0.125)] != "#" and self.row-int(self.row) == 0:
                self.col -= 0.125
                moving = True
        elif self.direction == "right":
            if level.tiles[int(self.row)][int(self.col+1)] != "#" and self.row-int(self.row) == 0:
                self.col += 0.125
                moving = True

        if level.tiles[int(self.row)][int(self.col)] == " ":
            level.tiles[int(self.row)][int(self.col)] = "."
            self.point += 10
            #run = True
            #templist = []
            #while run:
                #try:
                    #templist.append(level.tiles[self.row][self.col])
                    #level.tiles[self.row].pop(self.col)
                #except:
                    #run = False
            
            #for i in range(len(templist)-1):
                #level.tiles[self.row].append(templist[i+1])
            
            #level.tiles[self.row] = level.tiles[self.row][:self.col] + ["p"] + level.tiles[self.row][self.col+1:]

            #if level.tiles[int(self.row)][int(self.col)] != "<":
                #self.row == x-coordinate to >
                #self.col == y-coordinate to >
            #if level.tiles[int(self.row)][int(self.col)] != ">":
                #self.row == coordinate to <
                #self.col == coordinate to <

        if moving:
            if self.tick%2 == 0:
                self.sound_move0.play()
            else:
                self.sound_move1.play()

        self.tick += 1 
    
    def draw(self,screen, direction, ghostr, ghostc, state):

        # Draw pacman
        self.state = state

        if ghostr == self.row and ghostc == self.col:
            self.state = "LOAD"
            #self.row = self.start[0]
            #self.col = self.start[1]

        r = self.tick%6

        if self.direction == "left":
            screen.blit(self.images[r], (self.col*32, self.row*32))
        elif self.direction == "right":
            screen.blit(pg.transform.rotate(self.images[r],180), (self.col*32, self.row*32))
        elif self.direction == "up":
            screen.blit(pg.transform.rotate(self.images[r],-90), (self.col*32, self.row*32))
        elif self.direction == "down":
            screen.blit(pg.transform.rotate(self.images[r],90), (self.col*32, self.row*32))
        else:
            screen.blit(self.images[0], (self.col*32, self.row*32))  