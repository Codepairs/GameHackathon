import enum
import numpy as np
import random

class Direction(enum.Enum):
    north = 0
    east = 1
    south = 2
    west = 3

class Algo:
    def __init__(self):
        self.possible_directions_dictionary = \
                                    {'north': [Direction.west, Direction.north, Direction.east],
                                     'east': [Direction.north, Direction.east, ],
                                     'south': [Direction.east, Direction.south, Direction.west],
                                     'west': [Direction.north, Direction.west, Direction.south]}


    @staticmethod
    def check_enemies_by_direction(whole_map, ship_coordinates, ship_direction, ship_speed):
        pass

    @staticmethod
    def check_zone_by_direction():
        pass

    @staticmethod
    def check_north(whole_map, ship_coordinates, distance):
        if ((ship_coordinates[0] - distance) > 0 and
                whole_map[ship_coordinates[0] - distance][ship_coordinates[1]] == 0):
            return True
        return False

    @staticmethod
    def check_east(whole_map, ship_coordinates, distance):
        if ((ship_coordinates[1] + distance) > 0 and
                whole_map[ship_coordinates[0]][ship_coordinates[1] + distance] == 0):
            return True
        return False

    @staticmethod
    def check_south(whole_map, ship_coordinates, distance):
        if ((ship_coordinates[0] + distance) > 0 and
                whole_map[ship_coordinates[0] + distance][ship_coordinates[1]] == 0):
            return True
        return False

    @staticmethod
    def check_west(whole_map, ship_coordinates, distance):
        if ((ship_coordinates[1] - distance) > 0 and
        whole_map[ship_coordinates[0]][ship_coordinates[1] - distance] == 0):
            return True
        return False

    @staticmethod
    def check_north_max(whole_map, ship_coordinates, ship_speed, ship_size, directions_weights):
        direction_degrees = 0
        delta_speed = 0

        north_free = Algo.check_north(whole_map, ship_coordinates, ship_speed * ship_speed//4 + ship_size)
        east_free = Algo.check_east(whole_map, ship_coordinates, ship_speed * ship_speed//8 + ship_size)
        west_free = Algo.check_west(whole_map, ship_coordinates, ship_speed * ship_speed//8  + ship_size)

        max_points = max(north_free*directions_weights[0], east_free*directions_weights[1], west_free*directions_weights[3])

        if north_free*directions_weights[0]==max_points:
            delta_speed += 5

        elif (east_free*directions_weights[1]==max_points):
            direction_degrees = 90
            delta_speed -= 5

        else:
            direction_degrees = -90
            delta_speed -= 5
        #ship_speed = ship_speed % 20 + ship_speed // 20 * 20
        return [delta_speed, direction_degrees]

    @staticmethod
    def check_east_max(whole_map, ship_coordinates, ship_speed, ship_size, directions_weights):
        direction_degrees = 0
        delta_speed = 0
        east_free = Algo.check_east(whole_map, ship_coordinates, ship_speed * ship_speed//4 + ship_size)
        north_free = Algo.check_north(whole_map, ship_coordinates, ship_speed * ship_speed//8  + ship_size)
        south_free = Algo.check_south(whole_map, ship_coordinates, ship_speed * ship_speed//8  + ship_size)

        max_points = max(north_free * directions_weights[0], east_free * directions_weights[1],
                         south_free * directions_weights[2])

        if east_free * directions_weights[1] == max_points:
            delta_speed += 5

        elif (north_free * directions_weights[0] == max_points):
            direction_degrees = -90
            delta_speed -= 5

        else:
            direction_degrees = 90
            delta_speed -= 5
        #ship_speed = ship_speed % 20 + ship_speed // 20 * 20
        return [delta_speed, direction_degrees]

    @staticmethod
    def check_south_max(whole_map, ship_coordinates, ship_speed, ship_size, directions_weights):
        direction_degrees = 0
        delta_speed = 0
        south_free = Algo.check_south(whole_map, ship_coordinates, ship_speed * ship_speed//4 + ship_size)
        east_free = Algo.check_east(whole_map, ship_coordinates, ship_speed * ship_speed//8  + ship_size)
        west_free = Algo.check_west(whole_map, ship_coordinates, ship_speed * ship_speed//8 + ship_size)

        max_points = max(south_free * directions_weights[2], east_free * directions_weights[1],
                         west_free * directions_weights[3])

        if south_free * directions_weights[2] == max_points:
            delta_speed += 5

        elif (east_free * directions_weights[1] == max_points):
            direction_degrees = -90
            delta_speed -= 5

        else:
            direction_degrees = 90
            delta_speed -= 5
        #ship_speed = ship_speed % 20 + ship_speed // 20 * 20
        return [delta_speed, direction_degrees]

    @staticmethod
    def check_west_max(whole_map, ship_coordinates, ship_speed, ship_size, directions_weights):
        direction_degrees = 0
        delta_speed = 0
        north_free = Algo.check_north(whole_map, ship_coordinates, ship_speed * ship_speed//4 + ship_size)
        south_free = Algo.check_south(whole_map, ship_coordinates, ship_speed * ship_speed//8  + ship_size)
        west_free = Algo.check_west(whole_map, ship_coordinates, ship_speed * ship_speed//8  + ship_size)

        max_points = max(north_free * directions_weights[0], south_free * directions_weights[2],
                         west_free * directions_weights[3])

        if west_free * directions_weights[3] == max_points:
            delta_speed += 5

        elif (south_free * directions_weights[2] == max_points):
            direction_degrees = -90
            delta_speed -= 5

        else:
            direction_degrees = 90
            delta_speed -= 5
        #ship_speed = ship_speed % 20 + ship_speed // 20 * 20
        return [delta_speed, direction_degrees]

    # по сути мы знаем координаты всех островов. значит, известна зона, куда лучше не идти.
    # другими словами, не нужно вырывать часть матрицы и считать каждую клетку, достаточно проверить потенциальный ход
    # условно if whole_map[potential_move]==0: make_move
    # мы также можем потенциально заранее понять, стоит ли нам двигаться в каком-либо направлении
    # достаточно проверять зону через скорость*2

    # смотрю направление движения начальное -> ПРОВЕРЯЮ ДОСТУПНЫЕ ПОВОРОТЫ И ДВИЖЕНИЯ через взвешенный массив
    # -> проверяю их доступность
    @staticmethod
    def make_move_to_zone(whole_map, ship_coordinates, ship_direction_string, ship_speed, ship_size, directions_weights):
        direction_degrees = 0
        ship_direction = Direction[ship_direction_string].value
        match (ship_direction):
            case Direction.north.value:
                return Algo.check_north_max(whole_map, ship_coordinates, ship_speed, ship_size, directions_weights)

            case Direction.east.value:  # 'east':
                return Algo.check_east_max(whole_map, ship_coordinates, ship_speed, ship_size, directions_weights)


            case Direction.south.value:  # "'south':
                return Algo.check_south_max(whole_map, ship_coordinates, ship_speed, ship_size, directions_weights)

            case Direction.west.value:  # 'west':
                return Algo.check_east_max(whole_map, ship_coordinates, ship_speed, ship_size, directions_weights)



    @staticmethod
    def make_move(whole_map, ship_coordinates, ship_direction_string, ship_speed, ship_size):
        direction_degrees = 0
        delta_zone = 0
        ship_direction = Direction[ship_direction_string].value
        match(ship_direction):
            case Direction.north.value:
                if (Algo.check_north(whole_map, ship_coordinates, ship_speed*2 + ship_size)):
                    delta_zone +=5

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    direction_degrees = 90
                    delta_zone -=5

                elif (Algo.check_west(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    direction_degrees = -90
                    delta_zone -=5

            case Direction.east.value:  # 'east':
                if (Algo.check_east(whole_map, ship_coordinates, ship_speed*2 + ship_size)):
                    delta_zone +=5

                elif (Algo.check_south(whole_map, ship_coordinates, ship_speed//2 + ship_size )):
                    direction_degrees = 90
                    delta_zone -=5

                elif (Algo.check_north(whole_map, ship_coordinates, ship_speed//2 + ship_size )):
                    direction_degrees = -90
                    delta_zone -=5

            case Direction.south.value:  # "'south':
                if (Algo.check_south(whole_map, ship_coordinates, ship_speed*2 + ship_size)):
                    delta_zone +=5

                elif (Algo.check_west(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    direction_degrees = 90
                    delta_zone -=5

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    direction_degrees = -90
                    delta_zone -=5

            case Direction.west.value:  # 'west':
                if (Algo.check_west(whole_map, ship_coordinates, ship_speed*2 + ship_size)):
                    delta_zone +=5

                elif (Algo.check_north(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    direction_degrees = 90
                    delta_zone -=5

                elif (Algo.check_south(whole_map, ship_coordinates, ship_speed)):
                    direction_degrees = -90
                    delta_zone -=5
        #ship_speed = ship_speed % 20 + ship_speed // 20 * 20 #check if speed is close to max
        return [delta_zone, direction_degrees]

if __name__ == '__main__':
    print(Direction.south.value)
    #print()
