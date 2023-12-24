import requests
import numpy as np

class Map:
    def __init__(self):
        self.map = np.zeros([2000, 2000])


    def setup_map(self, url):
        islands_map = requests.get(url).json()
        islands = islands_map['islands']

        for island in islands:
            matrix: np.array = np.array(island['map'])
            island_x = island['start'][0]
            island_y = island['start'][1]
            for j in range(island_y, matrix.shape[0]):
                for i in range(island_x, matrix.shape[1]):
                    self.map[j][i] = 1


    def get_map(self):
        return self.map

