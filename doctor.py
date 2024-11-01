import pygame as pg
from maze import Grid

pg.init()
SCREEN = pg.math.Vector2(500, 500)
screen = pg.display.set_mode(SCREEN)
clock = pg.time.Clock()
running = True
grid = Grid(SCREEN, 20, screen)
grid.genMazeDFS()

while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Update
    # Render
    screen.fill("black")
    grid.render()
    pg.display.flip()
    clock.tick(60)

pg.quit()
