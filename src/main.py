import random
import time
from pprint import pprint
from GameAPIClass import GameAPI
from GameMapClass import GameMap
from AlgoClass import Algo
from BotClass import Bot
import threading


if __name__ == '__main__':
    server = GameAPI()
    server.deathmatch_registration_request()
    world_map = server.map_request()
    visual = GameMap(world_map)
    threading.Thread(target=visual.__init__).start()
    my_ships, enemy_ships, tick, zone = server.scan_around_ships_requests()
    while len(my_ships) > 0:
        my_ships, enemy_ships, tick, zone = server.scan_around_ships_requests()
        visual.set_ships(my_ships)
        visual.set_enemy_ships(enemy_ships)
        tick_changes = []
        for ship in my_ships:
            bot = Bot(ship)
            attack_coordinates = None, None
            if len(enemy_ships) != 0:
                attack_coordinates = bot.attack_opponents(enemy_ships)
                visual.render_shots(attack_coordinates)
            changes = server.create_changes(ship['id'], changeSpeed=3, rotate=None, x=attack_coordinates[1], y=attack_coordinates[0])
            tick_changes.append(changes)
        server.scan_at_point_request(random.randint(0, 2000), random.randint(0, 2000))
        server.ships_control_request(tick_changes)
        my_ships, enemy_ships, tick, zone = server.scan_around_ships_requests()
        visual.set_ships(my_ships)
        visual.set_enemy_ships(enemy_ships)
        visual.render(my_ships, enemy_ships)
        pprint(f"Союзный первый: {my_ships[0]['direction']}  {my_ships[0]['speed']} {my_ships[0]['scanRadius']}")





