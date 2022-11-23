import pygame as pg

class Level:

    def __init__(self, file):

        self.tiles = []
        with open(file, "r") as level_file:
            for line in level_file:
                line = line.rstrip("\r\n") # Remove line endings
                row = []
                for character in line:
                    row.append(character)
                self.tiles.append(row)


    def draw(self, screen, pacman):
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 1)
                elif tile == " ":
                    pg.draw.circle(screen,(220,220,0), (col_idx*32+16, row_idx*32+16),5)
        font = pg.font.SysFont("arial", 32)
        score = font.render(f"Points: {pacman.point}", True, (255,255,255))
        screen.blit(score, (5,5))

        

        