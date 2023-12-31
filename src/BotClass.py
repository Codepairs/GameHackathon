import enum
import random
import math
from AlgoClass import Algo


class Direction(enum.Enum):
    north = 0
    east = 1
    south = 2
    west = 3


class Bot:
    def __init__(self, ship, map):
        self.scan_radius = ship["scanRadius"]
        self.attack_radius = ship["cannonRadius"]
        self.speed = ship["speed"]
        self.direction = self.get_random_direction() if self.speed == 0 else ship["direction"]
        self.size = ship["size"]
        self.algorithm = Algo()
        self.coordinates = [ship["x"], ship["y"]]
        self.ship_id = ship["id"]
        self.direction_weights = [1, 1, 1, 1]  # north, east, south, west

        self.map = map

    def make_area_from_radius(self, whole_map, radius, coords):
        self.map = whole_map[coords[1] - radius:coords[1] + radius, coords[0] - radius:coords[0] + radius]

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def calculate_direction_weights(self, zone_center_coords):
        # ship_x = self.coordinates[1]
        # ship_y = self.coordinates[0]
        distance = math.sqrt(math.pow(zone_center_coords[0] - self.coordinates[0], 2)
                             + math.pow(zone_center_coords[1] - self.coordinates[1], 2))
        cos = distance / (zone_center_coords[1] - self.coordinates[1])
        sin = distance / (zone_center_coords[0] - self.coordinates[0])

        if (cos > 0 and sin > 0):
            self.direction_weights = [3, 3, 1, 1]

        if (cos > 0 and sin < 0):
            self.direction_weights = [1, 3, 3, 1]

        if (cos < 0 and sin < 0):
            self.direction_weights = [1, 1, 3, 3]

        if (cos < 0 and sin > 0):
            self.direction_weights = [3, 1, 1, 3]
        print("DIRECTION WEIGHTS", self.direction_weights)

    def get_random_direction(self):
        # direction_value = random.randint(0, 3)
        #direction_value = self.ship_id
        #direction_value = direction_value % 4
        direction_value = 1
        return Direction(direction_value).name

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_map(self, map):
        self.map = map

    def get_map(self):
        return self.map

    def set_coordinates(self, coords):
        self.coordinates = coords

    def get_coordinates(self):
        return self.coordinates

    def check_acceleration(self):
        if self.direction == 1:
            pass

    def make_move(self):
        # coefficient = self.size

        new_speed, new_direction = self.algorithm.make_move(self.map, self.coordinates, self.direction, self.speed,
                                                            self.size)
        if new_direction == 0:
            new_direction = None
        return new_speed, new_direction

    def make_move_to_zone(self):
        new_speed, new_direction = self.algorithm.make_move_to_zone(self.map, self.coordinates, self.direction,
                                                                    self.speed, self.size, self.direction_weights)
        if new_direction == 0:
            new_direction = None
        return new_speed, new_direction

    def choose_closest(self, enemy_ships):
        closest_enemy_ship = None
        minimal_distance = 100000000000
        for enemy_ship in enemy_ships:
            current_distance = math.sqrt(math.pow(enemy_ship["x"] - self.coordinates[0], 2)
                                         + math.pow(enemy_ship["y"] - self.coordinates[1], 2))
            if current_distance < minimal_distance:
                minimal_distance = current_distance
                closest_enemy_ship = enemy_ship
        return closest_enemy_ship

    """
    def attack_opponents(self, enemy_ships):
        closest_enemy_ship = self.choose_closest(enemy_ships)
        attack_coords = [closest_enemy_ship['x'], closest_enemy_ship['y']]
        distance = math.sqrt(math.pow(attack_coords[0] - self.coordinates[0], 2)
                             + math.pow(attack_coords[1] - self.coordinates[1], 2))
        if self.attack_radius < distance:
            cos = distance / (attack_coords[1] - self.coordinates[1])
            sin = distance / (attack_coords[0] - self.coordinates[0])

            attack_coords[0] = (int)(self.attack_radius * sin)  # y
            attack_coords[1] = (int)(self.attack_radius * cos)  # x
        return attack_coords
        """

    def attack_opponents(self, enemy_ships):
        if len(enemy_ships) == 0:
            attack_coords = [None, None]
            return attack_coords
        closest_enemy_ship = self.choose_closest(enemy_ships)
        attack_coords = [closest_enemy_ship['x'], closest_enemy_ship['y']]
        distance = math.sqrt(math.pow(attack_coords[0] - self.coordinates[0], 2)
                             + math.pow(attack_coords[1] - self.coordinates[1], 2))

        enemy_speed = closest_enemy_ship['speed']
        enemy_direction = closest_enemy_ship['direction']
        if enemy_speed > 0 and enemy_direction == 0:
            attack_coords[0] -= enemy_speed
        if enemy_speed > 0 and enemy_direction == 1:
            attack_coords[1] += enemy_speed
        if enemy_speed > 0 and enemy_direction == 2:
            attack_coords[0] += enemy_speed
        if enemy_speed > 0 and enemy_direction == 3:
            attack_coords[1] -= enemy_speed
            # Если скорость меньше 0 то изменение координат корабля будетобратно изменению координат при положительной скорости
        if enemy_speed < 0 and enemy_direction == 0:
            attack_coords[0] += enemy_speed
        if enemy_speed < 0 and enemy_direction == 1:
            attack_coords[1] -= enemy_speed
        if enemy_speed < 0 and enemy_direction == 2:
            attack_coords[0] -= enemy_speed
        if enemy_speed < 0 and enemy_direction == 3:
            attack_coords[1] += enemy_speed

        print(self.coordinates, attack_coords, closest_enemy_ship['x'], closest_enemy_ship['y'])

        if distance < self.attack_radius:

            attack_coords[0] = closest_enemy_ship['x']
            attack_coords[1] = closest_enemy_ship['y']
        else:
            attack_coords = [None, None]
            return attack_coords
        return attack_coords


def output(matrix, coords):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if (i, j) == (coords[0], coords[1]):
                print('X', end='')
                continue
            print(matrix[i][j], end='')
        print()
    print()


"""
if __name__=='__main__':
    matrix = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 1, 0, 1]]
    n = len(matrix[0])
    bot = Bot(matrix, 1, 0, [n//2, n//2])

    output(matrix, [len(matrix[0])//2, len(matrix[0])//2])

    for i in range(5):
        coords, new_direction = bot.make_move()
        bot.set_coordinates(coords)
        bot.set_direction(new_direction)
        output(matrix, coords)
        """
