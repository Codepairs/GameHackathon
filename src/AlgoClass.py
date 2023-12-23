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
<<<<<<< HEAD
    def check_direction(area, coordinates, direction, speed):
        if direction == 0:
            # 'north':
            if (coordinates[0] - speed > 0 and area[coordinates[0] - speed][coordinates[1]] == 0):
                coordinates[0] -= speed

            else:
                direction = 1

        if direction == 1:  # 'east':
            if (area[coordinates[0]][coordinates[1] + speed] == 0):
                coordinates[1] += 1

            else:
                direction = 2

        if direction == 2:  # "'south':
            if (area[coordinates[0] + speed][coordinates[1]] == 0):
                coordinates[0] += 1

            else:
                direction = 3

        if direction == 3:  # 'west':
            if (area[coordinates[0]][coordinates[1] - 1] == 0):
                coordinates[1] -= 1
            else:
                direction = 0

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
        coefficient = 2
        match(ship_direction):
            case Direction.north.value:
                if (Algo.check_north(whole_map, ship_coordinates, ship_speed*coefficient)):
                    ship_coordinates[0] -= ship_speed

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 1

<<<<<<< HEAD
<<<<<<< HEAD
            if direction==1: #'east':
                if (area[coordinates[0]][coordinates[1]+speed] == 0):
                    coordinates[1] += speed
=======
                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed)):
=======
                elif (Algo.check_west(whole_map, ship_coordinates, ship_speed)):
>>>>>>> s44w
                    ship_direction = 3
>>>>>>> s44w

            case Direction.east.value:  # 'east':
                if (Algo.check_east(whole_map, ship_coordinates, ship_speed * coefficient)):
                    ship_coordinates[1] += ship_speed

<<<<<<< HEAD
            if direction==2: #"'south':
                if (area[coordinates[0]+speed][coordinates[1]] == 0):
                    coordinates[0] += speed
=======
                elif (Algo.check_south(whole_map, ship_coordinates, ship_speed )):
                    ship_direction = 2
>>>>>>> s44w

                elif (Algo.check_north(whole_map, ship_coordinates, ship_speed )):
                    ship_direction = 0

<<<<<<< HEAD
<<<<<<< HEAD
            if direction==3: #'west':
                if (area[coordinates[0]][coordinates[1] - speed] == 0):
                    coordinates[1] -= speed
                else:
                    direction = 0
                    changing_direction_count+=1
=======
            elif ship_direction == Direction.south.value:  # "'south':
=======
            case Direction.south.value:  # "'south':
>>>>>>> s44w
                if (Algo.check_south(whole_map, ship_coordinates, ship_speed * coefficient)):
                    ship_coordinates[0] += ship_speed
>>>>>>> s44w

                elif (Algo.check_east(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 1

<<<<<<< HEAD
        return [coordinates, direction]

    @staticmethod
    def setup_changes(id, speed, rotate, x, y):
        changes = {
            'id': id,
            'changeSpeed': speed,
            'rotate': rotate,
            'cannonShoot': {
                'x': x,
                'y': y
            }
        }
        return changes


=======
                elif (Algo.check_west(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 3

            case Direction.west.value:  # 'west':
                if (Algo.check_west(whole_map, ship_coordinates, ship_speed * coefficient)):
                    ship_coordinates[1] -= ship_speed

                elif (Algo.check_north(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 0

                elif (Algo.check_south(whole_map, ship_coordinates, ship_speed)):
                    ship_direction = 2

        return [ship_coordinates, ship_direction]

if __name__ == '__main__':
    print(Direction.north)
>>>>>>> s44w
