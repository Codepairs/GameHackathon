import numpy as np
import requests
import pygame as pg

size = w, h = 1600, 800
#flags = pg.FULLSCREEN | pg.DOUBLEBUF
screen = pg.display.set_mode(size)
pg.display.set_caption('Gamethon')

# Цвета
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)

water = pg.Color(224, 255, 255)
island = pg.Color(0, 139, 139)


class GameMap:
    def __init__(self, url):
        self.url = url
        # Константы основного алгоритма
        self.surface = screen
        self.width = w
        self.height = h
        self.cells_amount = self.cells_h, self.cells_w = (500, 500)
        self.cell_size = screen.get_size()[0] / self.cells_h

        '''
        islands_map = requests.get(self.url).json()
        width = islands_map['width']
        height = islands_map['height']
        slug = islands_map['slug']
        islands = islands_map['islands']
           for island in islands:
            island['map'] = np.array(island['map'])
            island_x = island['start'][0]
            island_y = island['start'][1]
            draw(island)
            '''

    def render_islands(self):
        islands_map = requests.get(self.url).json()
        islands = islands_map['islands']
        for island in islands:
            matrix: np.array = np.array(islands[0]['map'])
            island_x = island['start'][0]
            island_y = island['start'][1]
            self.draw_island(island_x, island_y, matrix)

    def draw_island(self, x, y, matrix):
       for i in range(matrix.shape[0]):
            pg.draw.rect(screen, (0, 255, 0), (x + i * self.cell_size, y + matrix.shape[1] * self.cell_size, self.cell_size+ 1,self.cell_size + 1))




