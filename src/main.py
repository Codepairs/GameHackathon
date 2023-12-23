import time
from pprint import pprint
from GameAPIClass import GameAPI
from AlgoClass import Algo


def main():
    coordinator = GameAPI()
    coordinator.deathmatch_registration_request()
    my_ships, enemy_ships, tick, zone = coordinator.scan_around_ships_requests()
    while len(my_ships) > 0:
        my_ships, enemy_ships, tick, zone = coordinator.scan_around_ships_requests()
        pprint(my_ships)
        time.sleep(10)


if __name__ == '__main__':
    server = GameAPI()
    server.deathmatch_registration_request()
    my_ships, enemy_ships, tick, zone = server.scan_around_ships_requests()
    pprint(my_ships[0])

    all_changes = []
    for ship in my_ships:
        changes = Algo.setup_changes(ship['id'], 3, 90, 0, 0)
        all_changes.append(changes)
    print(server.ships_control_request(all_changes))








