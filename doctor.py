from time import sleep
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
boxes = grid.boxes
print("Done getting objects")
doctor = Doctor(grid=obs)
doctor.initialize(obs)
hasBoxesPlaced = False

# setting up font
font_size = 36
font = pygame.font.SysFont(None, font_size)

while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if doctor.lives == 0 or len(boxes) == 0:
        #     if event.type == pg.KEYDOWN:
        #         if event.key == pygame.K_q:
        #             exit()
        #         if event.type == pygame.K_r:
        #             grid = Grid(SCREEN, 30, screen)
        #             grid.genMazeDFS()
        #             obs = grid.getObs()
        #             boxes = grid.boxes
        #             print("Done getting objects")
        #             doctor = Doctor(grid=obs)
        #             doctor.initialize(obs)
        #             hasBoxesPlaced = False
        #         else:
        #             continue
        # key = pygame.key.get_pressed()
        # while not (key[pygame.K_q] or key[pygame.K_r]):
        #     key = pygame.key.get_pressed()
        # if key[pygame.K_q]:
        #     exit()

    # Update
    # Render
    # Update player position with collision detection
    doctor.move(obs, boxes)

    # Draw everything
    screen.fill(BLACK)
    grid.render()
    doctor.draw(screen)

    if not hasBoxesPlaced:
        grid.placeBoxes()
        hasBoxesPlaced = True

    lives_text = font.render(f"lives left: {doctor.lives}", True, WHITE)

    text_x = SCREEN_WIDTH + 10  # 10 pixels from the right edge
    text_y = 10
    screen.blit(lives_text, (text_x, text_y))

    if doctor.lives == 0 or len(boxes) == 0:
        winStr = ""
        if doctor.lives == 0:
            winStr = "The doctor died You lost"
        else:
            winStr = "Lets get that bread gamers"

        help_text = font.render(winStr, True, WHITE)
        screen.blit(help_text, (text_x, text_y + 20))
        pygame.display.flip()
        sleep(2)
        exit()

        # reset the game
        grid.genMazeDFS()
        print("Done generating maze")

        obs = grid.getObs()
        print("Done getting objects")
        doctor = Doctor(grid=obs)
        doctor.initialize(obs)

    # for wall in TEMP_WALLS:
    #     pygame.draw.rect(screen, RED, wall)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)


pg.quit()
