import enum
import random


class Algo:

    def __init__(self, area=None, traj=0):
        if area is None:
            area = []
        self.area = area   #matrix [[0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 1, 0, 1] ]
        self.trajectory = traj #enum.Enum('traj', ['north', 'east', 'south', 'west'])
        self.coordinates = [len(area[0])//2, len(area[0])//2]



    def set_area(self, area):
        self.area = area
    def get_area(self):
        return self.area

    def choose_random_trajectory(self):
        self.trajectory = random.randint(0, 4)

    def get_trajectory(self):
        return self.trajectory

    def make_move(self): #speed is 1 now
        coords = self.coordinates[::]
        while coords == self.coordinates:

            if self.trajectory==0:
             #'north':
                if (self.area[self.coordinates[0]-1][self.coordinates[1]]==0):
                    self.coordinates[0]-=1

                else:
                    self.trajectory = 1

            if self.trajectory==1: #'east':
                if (self.area[self.coordinates[0]][self.coordinates[1]+1] == 0):
                    self.coordinates[1] += 1

                else:
                    self.trajectory = 2

            if self.trajectory==2: #"'south':
                if (self.area[self.coordinates[0]+1][self.coordinates[1]] == 0):
                    self.coordinates[0] += 1

                else:
                    self.trajectory = 3

            if self.trajectory==3: #'west':
                if (self.area[self.coordinates[0]][self.coordinates[1] - 1] == 0):
                    self.coordinates[1] -= 1
                else:
                    self.trajectory = 0

        return self.coordinates

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
    #print(matrix)
    bot = Algo(matrix)
    output(matrix, [len(matrix[0])//2, len(matrix[0])//2])

    for i in range(5):
        coords = bot.make_move()
        output(matrix, coords)









