class Camera:
    def __init__(self, pos_x, pos_y, width, height, map_size):
        self.x = pos_x
        self.y = pos_y
        self.w = width
        self.h = height
        self.center_x = pos_x + width / 2
        self.center_y = pos_y + height / 2
        self.default_w = width
        self.default_h = height
        self.map_size = map_size

    def set_map_size(self, map_size):
        self.map_size = map_size

    def in_bounds(self, x, y):
        return self.x <= x <= self.w + self.x and self.y <= y <= self.h + self.y

    def update(self, x, y):
        self.x += x
        self.y += y
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x + self.w > self.map_size[0]:
            self.x = self.map_size[0] - self.w
        if self.y + self.h > self.map_size[1]:
            self.y = self.map_size[1] - self.h
        self.center_x = self.x + self.w / 2
        self.center_y = self.y + self.h / 2

    def output(self):
        print(self.x, self.y, self.w, self.h)
