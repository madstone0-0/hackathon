import pygame as pg


class Grid:
    def __init__(self, windowSize, blockSize, screen) -> None:
        self.winSize = windowSize
        self.blockSize = blockSize
        self.gridSize = windowSize / blockSize
        self.screen = screen

    def render(self):
        for i in range(4):
            dimens = ()
            if (i + 1) % 2 == 0:
                dimens = (self.winSize[0], self.blockSize)
                pg.draw.rect(
                    self.screen,
                    (255, 0, 0),
                    pg.Rect(width=self.winSize[0], height=self.blockSize),
                )
            else:
                eimens = (self.winSize[0], self.blockSize)
                pg.draw.rect(
                    self.screen,
                    (255, 0, 0),
                    pg.Rect(width=self.blockSize, height=self.winSize[1]),
                )

            # if i < 2:
