import enum
import random

class Direction(enum.Enum):
    north = 0
    east = 1
    south = 2
    west = 3

class Algo:
    def __init__(self, ship_direction):
        self.possible_directions_dictionary = \
                                    {'north': [Direction.east, Direction.west],
                                     'east': [Direction.north, Direction.south],
                                     'south': [Direction.east, Direction.west],
                                     'west': [Direction.north, Direction.south]}

    @staticmethod
    def check_enemies_by_direction(whole_map, ship_coordinates, ship_direction, ship_speed):
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
    def make_move(whole_map, ship_coordinates, ship_direction, ship_speed):
        coords = ship_coordinates[::]
        coefficient = 2
        changing_direction_count = 0
        while coords == ship_coordinates:

            if (ship_direction == Direction.north.value):
                if (Algo.check_north(whole_map, ship_coordinates, ship_speed*coefficient)):
                    ship_coordinates[0] -= ship_speed

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 1

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 3

            elif ship_direction == Direction.east.value:  # 'east':
                if (Algo.check_east(whole_map, ship_coordinates, ship_speed * coefficient)):
                    ship_coordinates[1] += ship_speed

                elif (Algo.check_south(whole_map, ship_coordinates, ship_speed )):
                    ship_direction = 2

                elif (Algo.check_north(whole_map, ship_coordinates, ship_speed )):
                    ship_direction = 0

            elif ship_direction == Direction.south.value:  # "'south':
                if (Algo.check_south(whole_map, ship_coordinates, ship_speed * coefficient)):
                    ship_coordinates[0] += ship_speed

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 1

                elif (Algo.check_west(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 3

            elif ship_direction == Direction.west.value:  # 'west':
                if (Algo.check_west(whole_map, ship_coordinates, ship_speed * coefficient)):
                    ship_coordinates[1] -= ship_speed

                elif (Algo.check_north(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 0

                elif (Algo.check_south(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 2

        return [ship_coordinates, ship_direction]

if __name__ == '__main__':
    print(Direction.north)
