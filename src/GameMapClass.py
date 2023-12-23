import numpy as np
import requests
import pygame as pg

size = w, h = 1600, 800
flags = pg.FULLSCREEN | pg.DOUBLEBUF
screen = pg.display.set_mode(size,flags)
pg.display.set_caption('Gamethon')

# Цвета
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)

water_color = pg.Color(88,171,226)
island_color = pg.Color(236,229,28)


class GameMap:
    def __init__(self, url):
        self.url = url
        # Константы основного алгоритма
        self.surface = screen
        self.width = w
        self.height = h
        self.cells_amount = self.cells_h, self.cells_w = (2000, 2000)
        screen.fill(water_color)

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                if event.type == pg.K_q:
                    running = False
                    pg.quit()
            self.render_islands()
            pg.display.flip()

    def render_islands(self):
        islands_map = requests.get(self.url).json()
        islands = islands_map['islands']
        for island in islands:
            matrix: np.array = np.array(island['map'])
            island_x = island['start'][0]
            island_y = island['start'][1]
            pg.draw.rect(screen, island_color, (island_x, island_y, matrix.shape[0], matrix.shape[1]))





