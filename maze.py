import pygame as pg
import random
from constants import RED


class Grid:
    def __init__(self, windowSize, blockSize, screen) -> None:
        self.winSize = windowSize
        self.blockSize = blockSize
        self.gridSize = windowSize / blockSize
        self.screen = screen
        self.borders = [
            # Top border
            pg.Rect(0, 0, self.winSize[0], self.blockSize),
            # Bottom border
            pg.Rect(
                0, self.winSize[1] - self.blockSize, self.winSize[0], self.blockSize
            ),
            # Left border
            pg.Rect(0, 0, self.blockSize, self.winSize[1]),
            # Right border
            pg.Rect(
                self.winSize[0] - self.blockSize, 0, self.blockSize, self.winSize[1]
            ),
        ]

        self.grid = [
            [1 for _ in range(int(self.winSize[0]))]
            for _ in range(int(self.winSize[1]))
        ]
        self.frontier = []

    def getGrid(self):
        return self.grid

    def getObs(self):
        obs = []
        for row in self.grid:
            for i in row:
                if i != 0:
                    obs.append(i)
        return obs

    def render(self):
        grX, grY = self.gridSize

        for y in range(int(grY)):
            for x in range(int(grX)):
                cell = self.grid[y][x]
                if cell == 0:
                    continue
                pg.draw.rect(self.screen, RED, cell)

        # for border in self.borders:
        #     pg.draw.rect(self.screen, (0, 0, 0), border)

    def addFront(self, x, y):
        grX, grY = self.gridSize
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grX and 0 <= ny < grY and self.grid[ny][nx] == 1:
                if (nx, ny) not in self.frontier:
                    self.frontier.append((nx, ny))

    def getNeighbours(self, x, y):
        grX, grY = self.gridSize
        neighbors = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grX and 0 <= ny < grY and self.grid[ny][nx] == 0:
                neighbors.append((nx, ny))
        return neighbors

    def getUnvisited(self, x, y):
        grX, grY = self.gridSize
        ns = []
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]  # Up, Right, Down, Left

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grX and 0 <= ny < grY and self.grid[ny][nx] == 1:
                ns.append((nx, ny))

        return ns

    def genMazeDFS(self):
        grX, grY = self.gridSize

        stack = [(1, int(grY - 2))]
        self.grid[stack[0][1]][stack[0][0]] = 0

        while stack:
            x, y = stack[-1]
            neighbors = self.getUnvisited(x, y)

            if neighbors:
                nx, ny = random.choice(neighbors)
                self.grid[ny][nx] = 0  # Mark the neighbor as a passage
                self.grid[(y + ny) // 2][(x + nx) // 2] = 0  # Remove the wall between
                stack.append((nx, ny))
            else:
                stack.pop()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    self.grid[i][j] = pg.Rect(
                        i * self.blockSize,
                        j * self.blockSize,
                        self.blockSize,
                        self.blockSize,
                    )

    def genMaze(self):
        grX, grY = self.gridSize
        # sX, sY = (
        #     random.randint(0, int(self.winSize[0] - 1)),
        #     random.randint(0, int(self.winSize[1] - 1)),
        # )
        sX, sY = 1, int(grY - 2)

        # sX = (sX // 2) * 2 + 1
        # sY = (sY // 2) * 2 + 1

        self.grid[sY][sX] = 0
        self.addFront(sX, sY)

        while len(self.frontier) != 0:
            fx, fy = random.choice(self.frontier)
            self.frontier.remove((fx, fy))

            neighs = self.getNeighbours(fx, fy)
            if len(neighs) == 1:
                nx, ny = neighs[0]
                self.grid[fy][fx] = 0
                self.grid[(fy + ny) // 2][(fx + nx) // 2] = 0
                self.grid[ny][nx] = 0

                self.addFront(fx, fy)
