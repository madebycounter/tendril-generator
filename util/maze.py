import pygame
from random import random


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.columns = []
        self.rows = []

        self.fill(0)
        self.set_walls()

    def fill(self, val):
        for x in range(self.width + 1):
            self.columns.append([val] * self.height)

        for y in range(self.height + 1):
            self.rows.append([val] * self.width)

    def set_walls(self):
        for y in range(self.height):
            self.columns[0][y] = 1
            self.columns[self.width][y] = 1

        for x in range(self.width):
            self.rows[0][x] = 1
            self.rows[self.height][x] = 1

    def fill_random(self, col_prob=0.5, row_prob=0.5):
        for x in range(1, self.width):
            for y in range(self.height):
                self.columns[x][y] = 1 if random() < col_prob else 0

        for y in range(1, self.height):
            for x in range(self.width):
                self.rows[y][x] = 1 if random() < row_prob else 0

    def get_cardinal(self, cell, dir):
        x, y = cell

        if dir == "N":
            return self.rows[y][x]
        elif dir == "S":
            return self.rows[y + 1][x]
        elif dir == "E":
            return self.columns[x + 1][y]
        elif dir == "W":
            return self.columns[x][y]

    def get_directions(self, cell):
        x, y = cell

        N = self.rows[y][x]
        S = self.rows[y + 1][x]
        E = self.columns[x + 1][y]
        W = self.columns[x][y]

        return N, S, E, W

    def get_neighbors(self, cell):
        directions = self.get_directions(cell)
        neighbors = []

        if not directions[0]:
            neighbors.append((cell[0], cell[1] - 1))
        if not directions[1]:
            neighbors.append((cell[0], cell[1] + 1))
        if not directions[2]:
            neighbors.append((cell[0] + 1, cell[1]))
        if not directions[3]:
            neighbors.append((cell[0] - 1, cell[1]))

        return neighbors

    def draw(
        self,
        ctx,
        color=(255, 255, 255),
    ):
        cell_size = (ctx.size[0] / self.width, ctx.size[1] / self.height)

        for x, column in enumerate(self.columns):
            for y, wall in enumerate(column):
                if wall:
                    pygame.draw.line(
                        ctx.screen,
                        color,
                        (
                            x * cell_size[0] + ctx.posn[0],
                            y * cell_size[1] + ctx.posn[1],
                        ),
                        (
                            x * cell_size[0] + ctx.posn[0],
                            (y + 1) * cell_size[1] + ctx.posn[1],
                        ),
                    )

        for y, row in enumerate(self.rows):
            for x, wall in enumerate(row):
                if wall:
                    pygame.draw.line(
                        ctx.screen,
                        color,
                        (
                            x * cell_size[0] + ctx.posn[0],
                            y * cell_size[1] + ctx.posn[1],
                        ),
                        (
                            (x + 1) * cell_size[0] + ctx.posn[0],
                            y * cell_size[1] + ctx.posn[1],
                        ),
                    )

    def draw_cell(self, ctx, cell, color=(255, 0, 0)):
        cell_size = (ctx.size[0] / self.width, ctx.size[1] / self.height)

        cell_scale = 0.5
        cell_draw_size = (cell_size[0] * cell_scale, cell_size[0] * cell_scale)
        cell_margin = (
            (1 - cell_scale) * cell_size[0] / 2,
            (1 - cell_scale) * cell_size[1] / 2,
        )

        pygame.draw.rect(
            ctx.screen,
            color,
            (
                ctx.posn[0] + cell_margin[0] + cell[0] * cell_size[0] + 1,
                ctx.posn[1] + cell_margin[1] + cell[1] * cell_size[1] + 1,
                cell_draw_size[0],
                cell_draw_size[1],
            ),
        )
