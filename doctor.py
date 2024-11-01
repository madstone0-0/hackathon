import pygame as pg
from maze import Grid
from constants import *
from doctor_player import *
from pygame.locals import *

pg.init()
SCREEN = pg.math.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pg.display.set_mode(SCREEN, RESIZABLE)
clock = pg.time.Clock()
running = True
grid = Grid(SCREEN, 30, screen)
print("Generating maze")
grid.genMazeDFS()
print("Done generating maze")


obs = grid.getObs()
print("Done getting objects")
doctor = Doctor(grid=obs)
doctor.initialize(obs)

while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Update
    # Render
    # Update player position with collision detection
    doctor.move(obs)

    # Draw everything
    screen.fill(BLACK)
    grid.render()
    doctor.draw(screen)
    # for wall in TEMP_WALLS:
    #     pygame.draw.rect(screen, RED, wall)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)


pg.quit()
