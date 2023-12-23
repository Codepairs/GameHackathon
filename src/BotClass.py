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
    def __init__(self, scan_radius, attack_radius, speed, direction, coords):
        self.scan_radius = scan_radius
        self.attack_radius = attack_radius
        self.speed = speed
        self.direction = direction
        self.algorithm = Algo
        self.coordinates = coords
        self.matrix_area = []

    def make_area_from_radius(self, whole_map, radius, coords):
        self.matrix_area = whole_map[coords[1]-radius:coords[1] + radius, coords[0]-radius:coords[0] + radius]

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_random_direction(self):
        self.direction = random.randint(0, 4)


    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_area(self, area):
        self.matrix_area = area

    def get_area(self):
        return self.matrix_area

    def set_coordinates(self, coords):
        self.coordinates = coords

    def get_coordinates(self):
        return self.coordinates




    def make_move(self):
        coords = self.algorithm.make_move(self.matrix_area, self.coordinates, self.direction, self.speed)
        if coords==None:
            self.speed-=2
        return coords
        ''' to be continued'''

    def attack_opponents(self, opponent_coords, dir, speed):
        attack_coords = opponent_coords
        distance = math.sqrt(math.pow(opponent_coords[0]-self.coordinates[0],2)
                                          + math.pow(opponent_coords[1]-self.coordinates[0],2))
        if self.attack_radius < distance:
            cos = distance/(opponent_coords[1]-self.coordinates[1])
            sin = distance/(opponent_coords[0]-self.coordinates[0])

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
