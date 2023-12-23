import enum
import random

from AlgoClass import Algo

class Direction(enum.Enum):
    north = 0
    east = 1
    south = 2
    west = 3

class Bot:
    def __init__(self, area, speed, direction, coords):
        self.area = area
        self.speed = speed
        self.direction = direction
        self.algorithm = Algo
        self.coordinates = coords

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def choose_random_direction(self):
        self.direction = random.randint(0, 4)


    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_area(self, area):
        self.area = area

    def get_area(self):
        return self.area

    def set_coordinates(self, coords):
        self.coordinates = coords

    def get_coordinates(self):
        return self.coordinates

    def check_acceleration(self):
        if self.direction == 1:
            pass

    def make_move(self):
        coords = self.algorithm.make_move(self.area, self.coordinates, self.direction, self.speed)
        if coords==None:
            self.speed-=2
        return coords
        ''' to be continued'''

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
