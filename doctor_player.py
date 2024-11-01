import pygame
from constants import *
from random import randint


class Doctor:
    def __init__(self, x=0, y=0, speed=5, lives=2, grid=None):
        self.rect = pygame.Rect(x, y, *DOCTOR_SIZE)
        self.speed = speed
        self.lives = lives
        self.grid = grid

    def initialize(self, walls):
        init_x, init_y = randint(2, SCREEN_WIDTH - 2), randint(2, SCREEN_HEIGHT - 2)
        temp_rect = pygame.Rect(init_x, init_y, DOCTOR_SIZE[0] - 2, DOCTOR_SIZE[1] - 2)
        width = walls[0].width
        print("Checking for collisions")
        collisons = 0
        while any(temp_rect.colliderect(wall) for wall in self.grid):
            if collisons > 100:
                print("Too many collisions")
                return self.initialize(walls)
            temp_rect.x += width
            temp_rect.y += width
            collisons += 1
            print(collisons)
        print("Done checking for collisions")
        self.rect = temp_rect

    def move(self, walls=None, boxes=None):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        # if walls is not none
        if walls:
            new_rect = self.rect.move(dx, dy)
            if not any(new_rect.colliderect(wall) for wall in walls):
                self.rect = new_rect

        # keep us within bounds
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

        # check if we have collided with a box
        if boxes:
            for i in range(len(boxes)):
                if self.rect.colliderect(boxes[i]):
                    if boxes[i].isApple:
                        self.lives -= 1
                    else:
                        self.lives += 1
                    boxes.pop(i)
                    break

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
