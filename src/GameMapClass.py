from CameraClass import Camera
import requests
import pygame as pg
import json
from BotClass import Bot
from MapCLass import Map

white = pg.Color(255, 255, 255)
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)
purple = pg.Color(255, 0, 255)

enemy_scan_color = white
ally_scan_color = white
ally_attack_color = green
enemy_attack_color = red
projectile_color = pg.Color(255, 255, 0)
enemy_ship_color = pg.Color(128, 0, 0)
ally_ship_color = pg.Color(64, 89, 19)
water_color = pg.Color(157, 78, 221)
island_color = pg.Color(36, 0, 70)


class GameMap:
    def __init__(self, url):
        pg.init()
        self.url = url
        self.ally_ships = None
        self.enemy_ships = None
        self.size = self.w, self.h = 1600, 800
        self.flags = (pg.RESIZABLE | pg.FULLSCREEN)
        self.screen = pg.display.set_mode(self.size, self.flags)
        self.running = True
        self.game_map = pg.Surface((2000, 2000))
        self.zoom = 1
        self.camera = Camera(0, 0, self.w, self.h, self.game_map.get_size())
        # self.island_map = requests.get(self.url).json()['islands']
        self.island_map = self.read_from_file()
        pg.display.set_caption('Gamethon')

    def read_from_file(self):
        with open('island_map.txt', 'r') as file:
            data = json.load(file)
            return data['islands']

    def scale(self, size):
        return size * self.zoom

    def set_ships(self, ships):
        self.ally_ships = ships

    def set_enemy_ships(self, ships):
        self.enemy_ships = ships

    def game_map_transform(self, zoom):
        self.game_map = pg.Surface((2000 * zoom, 2000 * zoom))
        self.camera.set_map_size(self.game_map.get_size())
        return self.game_map

    def render(self):
        self.game_map = self.game_map_transform(self.zoom)
        self.game_map.fill(water_color)
        self.render_enemy_ships()
        self.render_ally_ships()
        self.render_islands()
        self.render_attack()
        self.camera.output()
        self.screen.blit(
            self.game_map,
            (
                0,
                0
            ),
            (
                self.camera.x,
                self.camera.y,
                self.camera.w,
                self.camera.h)
        )
        pg.display.flip()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                        pg.quit()
                    if event.key == pg.K_d:
                        self.camera.update(self.scale(50), 0)
                    if event.key == pg.K_a:
                        self.camera.update(self.scale(-50), 0)
                    if event.key == pg.K_w:
                        self.camera.update(0, self.scale(-50))
                    if event.key == pg.K_s:
                        self.camera.update(0, self.scale(50))

                    if event.key == pg.K_MINUS:
                        self.zoom -= 1
                        if self.zoom <= 0:
                            self.zoom = 1
                    if event.key == pg.K_EQUALS:
                        self.zoom += 1
            if pg.key.get_pressed()[pg.K_RIGHT]:
                self.camera.update(self.scale(3), 0)
            if pg.key.get_pressed()[pg.K_LEFT]:
                self.camera.update(self.scale(-3), 0)
            if pg.key.get_pressed()[pg.K_UP]:
                self.camera.update(0, self.scale(-3))
            if pg.key.get_pressed()[pg.K_DOWN]:
                self.camera.update(0, self.scale(3))
            self.render()

    def render_attack(self):
        mapa = Map()
        global_map = mapa.generate_map(self.island_map)
        bots_list = []
        for ship in self.ally_ships:
            bots_list.append(Bot(ship, global_map))
        for bot in bots_list:
            attack_coordinates = bot.attack_opponents(self.enemy_ships)
            if attack_coordinates[0] is not None and attack_coordinates[1] is not None:
                pg.draw.rect(
                    self.game_map,
                    projectile_color,
                    (
                        self.scale(attack_coordinates[0]),
                        self.scale(attack_coordinates[1]),
                        self.scale(2),
                        self.scale(2)
                    )
                )

    def render_islands(self):
        for island in self.island_map:
            island_x = island['start'][0]
            island_y = island['start'][1]
            if not self.camera.in_bounds(self.scale(island_x), self.scale(island_y)):
                continue
            pg.draw.rect(
                self.game_map,
                island_color,
                (
                    self.scale(island_x),
                    self.scale(island_y),
                    self.scale(len(island['map'])),
                    self.scale(len(island['map'][0]))
                )
            )

    def render_ally_ships(self):
        for ship in self.ally_ships:
            if not self.camera.in_bounds(self.scale(ship['x']), self.scale(ship['y'])):
                continue
            scan_radius = ship['scanRadius']
            cannon_radius = ship['cannonRadius']
            pg.draw.circle(
                self.game_map,
                ally_attack_color,
                (
                    self.scale(ship['x']),
                    self.scale(ship['y'])
                ),
                self.scale(cannon_radius),
                self.scale(1)
            )
            pg.draw.circle(
                self.game_map,
                ally_scan_color,
                (
                    self.scale(ship['x']),
                    self.scale(ship['y'])
                ),
                self.scale(scan_radius),
                self.scale(1)
            )
            pg.draw.rect(
                self.game_map,
                ally_ship_color,
                (
                    self.scale(ship['x']),
                    self.scale(ship['y']),
                    self.scale(3),
                    self.scale(3)
                )
            )

    def render_enemy_ships(self):
        for ship in self.enemy_ships:
            if not self.camera.in_bounds(self.scale(ship['x']), self.scale(ship['y'])):
                continue
            enemy_scan = 60
            enemy_cannon_radius = 20
            pg.draw.circle(
                self.game_map,
                enemy_attack_color,
                (
                    self.scale(ship['x']),
                    self.scale(ship['y'])
                ),
                self.scale(enemy_cannon_radius),
                self.scale(1)
            )

            pg.draw.circle(
                self.game_map,
                enemy_scan_color,
                (
                    self.scale(ship['x']),
                    self.scale(ship['y'])
                ),
                self.scale(enemy_scan),
                self.scale(1)
            )
            pg.draw.rect(
                self.game_map,
                enemy_ship_color,
                (
                    self.scale(ship['x']),
                    self.scale(ship['y']),
                    self.scale(3),
                    self.scale(3)
                )
            )
