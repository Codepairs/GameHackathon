import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 10
WINDOW_SIZE = (2000, 2000)
BACKGROUND = (150, 90, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pg.display.set_mode(WINDOW_SIZE)

screen.fill(BACKGROUND)
r1 = pg.draw.rect(screen, BLACK, (20, 20, 60, 40))
r1 = pg.draw.rect(screen, WHITE, (40, 40, 80, 70))
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False