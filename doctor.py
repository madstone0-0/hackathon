import pygame as pg
from maze import Grid

pg.init()
SCREEN = pg.math.Vector2(1280, 720)
screen = pg.display.set_mode(SCREEN)
clock = pg.time.Clock()
running = True
grid = Grid(SCREEN, 10, screen)

while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Update
    # Render
    screen.fill("blue")
    # grid.render()
    pg.draw.rect(screen, (255, 0, 0), pg.Rect(30, 30, 60, 60))
    pg.display.flip()
    clock.tick(60)

pg.quit()
