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
gameWon = False
grid = Grid(SCREEN, 30, screen)
print("Generating maze")
grid.genMazeDFS()
print("Done generating maze")


obs = grid.getObs()
print("Done getting objects")
doctor = Doctor(grid=obs)
doctor.initialize(obs)

#setting up font
font_size = 36
font = pygame.font.SysFont(None, font_size)

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
    lives_text = font.render(f"lives left: {doctor.lives}", True, WHITE) 
    text_x = SCREEN_WIDTH - lives_text.get_width() - 10  # 10 pixels from the right edge
    text_y = 10
    screen.blit(lives_text, (text_x, text_y))

    # for wall in TEMP_WALLS:
    #     pygame.draw.rect(screen, RED, wall)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)


pg.quit()
