import time
from pprint import pprint
from GameAPIClass import GameAPI
from GameMapClass import GameMap
import pygame as pg
from GameMapClass import screen
import numpy as np

def main():
    coordinator = GameAPI()
    coordinator.deathmatch_registration_request()
    my_ships, enemy_ships, tick, zone = coordinator.scan_around_ships_requests()
    while len(my_ships) > 0:
        my_ships, enemy_ships, tick, zone = coordinator.scan_around_ships_requests()
        pprint(my_ships)
        time.sleep(10)


if __name__ == '__main__':
    pg.init()
    server = GameAPI()
    server.deathmatch_registration_request()
    islands_map = server.map_request()
    game_map = GameMap(islands_map)
    game_map.run()






