import enum
import random

class Direction(enum.Enum):
    north = 0
    east = 1
    south = 2
    west = 3

class Algo:
    def __init__(self):
        self.possible_directions_dictionary = \
                                    {'north': [Direction.east, Direction.west],
                                     'east': [Direction.north, Direction.south],
                                     'south': [Direction.east, Direction.west],
                                     'west': [Direction.north, Direction.south]}


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

    # по сути мы знаем координаты всех островов. значит, известна зона, куда лучше не идти.
    # другими словами, не нужно вырывать часть матрицы и считать каждую клетку, достаточно проверить потенциальный ход
    # условно if whole_map[potential_move]==0: make_move
    # мы также можем потенциально заранее понять, стоит ли нам двигаться в каком-либо направлении
    # достаточно проверять зону через скорость*2
    @staticmethod
    def make_move(whole_map, ship_coordinates, ship_direction_degrees, ship_speed, ship_size):
        match(ship_direction_degrees):
            case Direction.north.value:
                if (Algo.check_north(whole_map, ship_coordinates, ship_speed*2 + ship_size)):
                    ship_speed += 4

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    ship_direction_degrees = 90
                    ship_speed //= 2

                elif (Algo.check_west(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    ship_direction_degrees = -90
                    ship_speed //= 2

            case Direction.east.value:  # 'east':
                if (Algo.check_east(whole_map, ship_coordinates, ship_speed*2 + ship_size)):
                    ship_speed += 4

                elif (Algo.check_south(whole_map, ship_coordinates, ship_speed//2 + ship_size )):
                    ship_direction_degrees = 90
                    ship_speed //= 2

                elif (Algo.check_north(whole_map, ship_coordinates, ship_speed//2 + ship_size )):
                    ship_direction_degrees = -90
                    ship_speed //= 2

            case Direction.south.value:  # "'south':
                if (Algo.check_south(whole_map, ship_coordinates, ship_speed*2 + ship_size)):
                    ship_speed += 4

                elif (Algo.check_west(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    ship_direction_degrees = 90
                    ship_speed //= 2

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    ship_direction_degrees = -90
                    ship_speed //= 2

            case Direction.west.value:  # 'west':
                if (Algo.check_west(whole_map, ship_coordinates, ship_speed*2 + ship_size)):
                    ship_speed += 4

                elif (Algo.check_north(whole_map, ship_coordinates, ship_speed//2 + ship_size)):
                    ship_direction_degrees = 90
                    ship_speed //= 2

                elif (Algo.check_south(whole_map, ship_coordinates, ship_speed)):
                    ship_direction_degrees = -90
                    ship_speed //= 2
        ship_speed = ship_speed%10 + ship_speed//10 * 10 #check if speed is close to max
        return [ship_speed, ship_direction_degrees]

if __name__ == '__main__':
    print(Direction.north)
