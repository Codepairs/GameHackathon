import random
import numpy as np
import requests
import pygame as pg

white = pg.Color(255, 255, 255)
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)
purple = pg.Color(255, 0, 255)

water_color = pg.Color(88, 171, 226)
island_color = pg.Color(236, 229, 28)

class GameMap:
    def __init__(self, url):
        pg.init()
        self.url = url
        self.my_ships = None
        self.enemy_ships = None
        self.size = self.w, self.h = 1600, 800
        self.surface = pg.display.set_mode(self.size)
        self.window = pg.Surface((2000, 2000))
        pg.display.set_caption('Gamethon')

    def set_ships(self, ships):
        self.my_ships = ships

    def set_enemy_ships(self, ships):
        self.enemy_ships = ships

    def ships_changes_apply(self, tick_changes):
        pass

    def render(self, ally_ships, enemy_ships):
        self.set_ships(ally_ships)
        self.set_enemy_ships(enemy_ships)
        self.window.fill(water_color)
        self.render_ally_ships()
        self.render_enemy_ships()
        self.render_islands()
        resized_screen = pg.transform.scale(self.window, (self.w, self.h))
        self.surface.blit(resized_screen, (0, 0))
        pg.display.flip()


    def run(self):
        running = True
        self.render_islands()
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False
                    pg.quit()
            self.window.fill(water_color)
            self.render_ally_ships()
            self.render_islands()
            resized_screen = pg.transform.scale(self.window, (self.w, self.h))
            self.surface.blit(resized_screen, (0, 0))
            pg.display.flip()

    def render_shots(self, shot_coords):
        pg.draw.rect(self.window, blue, (shot_coords[0], shot_coords[1], 20, 20))
        resized_screen = pg.transform.scale(self.window, (self.w, self.h))
        self.surface.blit(resized_screen, (0, 0))
        pg.display.flip()

    def render_islands(self):
        islands_map = requests.get(self.url).json()
        islands = islands_map['islands']
        for island in islands:
            matrix: np.array = np.array(island['map'])
            island_x = island['start'][0]
            island_y = island['start'][1]
            pg.draw.rect(self.window, island_color, (island_x, island_y, matrix.shape[0], matrix.shape[1]))

    def render_ally_ships(self, counter= 0):
        for ship in self.my_ships:
            coordinates = ship['x'] + counter, ship['y'] + counter
            scan_radius = ship['scanRadius']
            cannon_radius = ship['cannonRadius']
            pg.draw.circle(self.window, green, coordinates, cannon_radius, 2)
            pg.draw.circle(self.window, white, coordinates, scan_radius, 3)
            pg.draw.rect(self.window, green, (coordinates[0], coordinates[1], 3, 3))

    def render_enemy_ships(self, counter=0):
        for ship in self.enemy_ships:
            coordinates = ship['x'] - counter, ship['y'] - counter
            enemy_scan = 60
            enemy_cannon_radius = 20
            pg.draw.circle(self.window, red , coordinates, enemy_cannon_radius, 2)
            pg.draw.circle(self.window, white, coordinates, enemy_scan, 3)
            pg.draw.rect(self.window, blue, (coordinates[0], coordinates[1], 3, 3))
