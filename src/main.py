import random
from pprint import pprint
from GameAPIClass import GameAPI
from GameMapClass import GameMap
from BotClass import Bot
from AlgoClass import Algo
from MapCLass import Map
import threading


if __name__ == '__main__':
    server = GameAPI()
    """
    Выбираем куда отправлять запрос, десматч или рояль
    """
    server.deathmatch_registration_request()
    #server.leave_request()
    #server.battleroyal_registration_request()

    # Получаем ссылку на карту в json
    world_map = server.map_request()
    visual = GameMap(world_map)
    threading.Thread(target=visual.__init__).start()
    # Сканим все вокруг
    my_ships, enemy_ships, tick, zone = server.scan_around_ships_requests()
    mapa = Map()
    global_map = mapa.setup_map(world_map)
    # Пока корабли живы
    while len(my_ships) > 0:
        my_ships, enemy_ships, tick, zone = server.scan_around_ships_requests()
        visual.set_ships(my_ships)
        visual.set_enemy_ships(enemy_ships)
        tick_changes = []
        # Для каждого корабля ставим ИИ
        for ship in my_ships:
            bot = Bot(ship, global_map)
            bot.set_random_direction()
            attack_coordinates = bot.attack_opponents(enemy_ships)
            # Атакуем если есть враги
            if attack_coordinates[0] is not None and attack_coordinates[1] is not None:
                visual.render_shots(attack_coordinates)
            """
            Тут выбор для десматча и рояля
            """
            #change_speed, rotate = bot.make_move_to_zone()
            change_speed, rotate = bot.make_move()
           # print(change_speed, rotate)
            print(f"Число попаданий: {ship['cannonShootSuccessCount']}")
            changes = server.create_changes(ship['id'], changeSpeed=change_speed, rotate=rotate, x=attack_coordinates[1], y=attack_coordinates[0])
            tick_changes.append(changes)
        server.scan_at_point_request(random.randint(0, 2000), random.randint(0, 2000))
        server.ships_control_request(tick_changes)
        my_ships, enemy_ships, tick, zone = server.scan_around_ships_requests()
        visual.set_ships(my_ships)
        visual.set_enemy_ships(enemy_ships)
        visual.render(my_ships, enemy_ships)
        pprint(f"Союзный первый: {my_ships[0]['direction']}  {my_ships[0]['speed']} {my_ships[0]['scanRadius']}")





