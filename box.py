import pygame
from constants import *
from main import *


class Box:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        # self.isApple = rng(2) == 1
        self.isApple = True
        # apple if = 1 else bread

    def draw(self, surface):
        pygame.draw.rect(surface, BROWN, self.rect)

