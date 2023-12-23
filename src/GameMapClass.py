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
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)

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
        self.render_islands()
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False
                    pg.quit()
            self.render_ships()
            pg.display.flip()

    def render_islands(self):
        islands_map = requests.get(self.url).json()
        islands = islands_map['islands']
        for island in islands:
            matrix: np.array = np.array(island['map'])
            island_x = island['start'][0]
            island_y = island['start'][1]
            pg.draw.rect(screen, island_color, (island_x, island_y, matrix.shape[0], matrix.shape[1]))

    def render_ships(self):
        ships = [{'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 4,
  'id': 2752,
  'maxChangeSpeed': 5,
  'maxHp': 4,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 4,
  'speed': 0,
  'x': 1428,
  'y': 1336},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 2,
  'id': 2759,
  'maxChangeSpeed': 5,
  'maxHp': 2,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 2,
  'speed': 0,
  'x': 1449,
  'y': 1336},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 2,
  'id': 2757,
  'maxChangeSpeed': 5,
  'maxHp': 2,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 2,
  'speed': 0,
  'x': 1443,
  'y': 1336},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 3,
  'id': 2758,
  'maxChangeSpeed': 5,
  'maxHp': 3,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 3,
  'speed': 0,
  'x': 1446,
  'y': 1336},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 2,
  'id': 2760,
  'maxChangeSpeed': 5,
  'maxHp': 2,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 2,
  'speed': 0,
  'x': 1452,
  'y': 1335},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 5,
  'id': 2753,
  'maxChangeSpeed': 5,
  'maxHp': 5,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 5,
  'speed': 0,
  'x': 1431,
  'y': 1336},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 3,
  'id': 2754,
  'maxChangeSpeed': 5,
  'maxHp': 3,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 3,
  'speed': 0,
  'x': 1434,
  'y': 1336},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 4,
  'id': 2755,
  'maxChangeSpeed': 5,
  'maxHp': 4,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 4,
  'speed': 0,
  'x': 1437,
  'y': 1337},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 2,
  'id': 2751,
  'maxChangeSpeed': 5,
  'maxHp': 2,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 2,
  'speed': 0,
  'x': 1425,
  'y': 1336},
                {'cannonCooldown': 3,
  'cannonCooldownLeft': 0,
  'cannonRadius': 20,
  'cannonShootSuccessCount': 0,
  'direction': 'north',
  'hp': 3,
  'id': 2756,
  'maxChangeSpeed': 5,
  'maxHp': 3,
  'maxSpeed': 10,
  'minSpeed': -1,
  'scanRadius': 60,
  'size': 3,
  'speed': 0,
  'x': 1440,
  'y': 1335}]
        for ship in ships:
            coordinates = ship['x']-1000, ship['y']-1000
            print(coordinates)
            scan_radius = ship['scanRadius']
            cannon_radius = ship['cannonRadius']
            pg.draw.circle(screen, red, coordinates, cannon_radius, 1)
            pg.draw.circle(screen, white, coordinates, scan_radius, 2)
            pg.draw.rect(screen, green, (coordinates[0], coordinates[1], 3, 3))


visual = GameMap('https://datsblack.datsteam.dev/json/map/6586ae233e7ba8.12192069.json')
visual.run()


