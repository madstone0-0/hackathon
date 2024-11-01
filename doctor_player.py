import pygame
from constants import *

class Doctor:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y)
        self.speed = 5
        

    def move(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y += self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y -= self.speed

        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
    
    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)