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
    def __init__(self, ship):
        self.scan_radius = ship["scanRadius"]
        self.attack_radius = ship["cannonRadius"]
        self.speed = ship["speed"]
        self.direction = ship["direction"]
        self.size = ship["size"]
        self.algorithm = Algo
        self.coordinates = [ship["x"], ship["y"]]
        self.direction_weights = [1,1,1,1] #north, east, south, west

    def make_area_from_radius(self, whole_map, radius, coords):
        self.radius = whole_map[coords[1] - radius:coords[1] + radius, coords[0] - radius:coords[0] + radius]

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def calculate_direction_weights(self, zone_center_coords):
        #ship_x = self.coordinates[1]
        #ship_y = self.coordinates[0]
        distance = math.sqrt(math.pow(zone_center_coords[0] - self.coordinates[0], 2)
                             + math.pow(zone_center_coords[1] - self.coordinates[1], 2))
        cos = distance / (zone_center_coords[1] - self.coordinates[1])
        sin = distance / (zone_center_coords[0] - self.coordinates[0])

        if (cos>0 and sin>0):
            self.direction_weights = [3, 3, 1, 1]

        if (cos > 0 and sin < 0):
            self.direction_weights = [1, 3, 3, 1]

        if (cos < 0 and sin < 0):
            self.direction_weights = [1, 1, 3, 3]

        if (cos < 0 and sin > 0):
            self.direction_weights = [3, 1, 1, 3]


    def set_random_direction(self):
        self.direction = random.randint(0, 4)


    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_area(self, area):
        self.radius = area

    def get_area(self):
        return self.radius

    def set_coordinates(self, coords):
        self.coordinates = coords

    def get_coordinates(self):
        return self.coordinates

    def check_acceleration(self):
        if self.direction == 1:
            pass

    def make_move(self):
        #coefficient = self.size

        new_speed, new_direction = self.algorithm.make_move(self.radius, self.coordinates, self.direction, self.speed, self.size)
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

    def attack_opponents(self, enemy_ships):
        closest_enemy_ship = self.choose_closest(enemy_ships)
        attack_coords = [closest_enemy_ship['x'], closest_enemy_ship['y']]
        distance = math.sqrt(math.pow(attack_coords[0]-self.coordinates[0],2)
                                          + math.pow(attack_coords[1]-self.coordinates[1] ,2))
        if self.attack_radius < distance:
            cos = distance/(attack_coords[1]-self.coordinates[1])
            sin = distance/(attack_coords[0]-self.coordinates[0])

            attack_coords[0] = (int) (self.attack_radius*sin) # y
            attack_coords[1] = (int) (self.attack_radius*cos) # x
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
