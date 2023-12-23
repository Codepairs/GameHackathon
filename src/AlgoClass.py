import enum
import random


class Algo:
    @staticmethod
    def check_direction(area, coordinates, direction, speed):
<<<<<<< HEAD
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
=======
        pass
>>>>>>> s44w

    @staticmethod
    def make_move(area, coordinates, direction, speed): #speed is 1 now
        coords = coordinates[::]
        changing_direction_count = 0
        while coords==coordinates:

            if direction==0:
             #'north':
                if (coordinates[0]-speed>0 and  area[coordinates[0]-speed][coordinates[1]]==0):
                    coordinates[0]-=speed

                else:
                    direction = 1
                    changing_direction_count+=1

            if direction==1: #'east':
                if (area[coordinates[0]][coordinates[1]+speed] == 0):
                    coordinates[1] += speed

                else:
                    direction = 2
                    changing_direction_count+=1

            if direction==2: #"'south':
                if (area[coordinates[0]+speed][coordinates[1]] == 0):
                    coordinates[0] += speed

                else:
                    direction = 3
                    changing_direction_count+=1

            if direction==3: #'west':
                if (area[coordinates[0]][coordinates[1] - speed] == 0):
                    coordinates[1] -= speed
                else:
                    direction = 0
                    changing_direction_count+=1

            if changing_direction_count==4:
                return None

        return [coordinates, direction]