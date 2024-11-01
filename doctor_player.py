import pygame
from constants import *

class Doctor:
    def __init__(self, x = 0, y = 0, speed = 5, lives = 2):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = speed
        self.lives = lives
        
    def initialize(self, walls):
        init_x, init_y = 0, SCREEN_HEIGHT
        temp_rect = pygame.Rect(init_x, init_y, 50, 50)
        width = walls[0].width
        while any(temp_rect.colliderect(wall) for wall in TEMP_WALLS):
                temp_rect.x+width
        self.rect = temp_rect


    def move(self, walls = None):
        keys = pygame.key.get_pressed() 
        dx, dy = 0,0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        #if walls is not none
        if walls:
            new_rect = self.rect.move(dx, dy)
            if not any(new_rect.colliderect(wall) for wall in walls):
                self.rect = new_rect
        
        #keep us within bounds
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    
    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

    def die(self):
        self.lives -=1
    
    def revive(self):
        self.lives+=1
