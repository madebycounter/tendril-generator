from util.maze import Maze
from util.bfs import bfs
from util.grid import grid_neighbors
from util.smooth import b_spline
import pygame


class Tendril:
    def __init__(
        self, aspect_ratio, maze_resolution=50, resolution=50, maze_density=[0.2, 0.7]
    ):
        self.aspect_ratio = aspect_ratio
        self.maze_resolution = maze_resolution
        self.resolution = resolution
        self.maze_density = maze_density

        self.maze = None
        self.solve1 = []
        self.solve2 = []
        self.path = []

    def draw(self, ctx, color=(255, 0, 0), width=5):
        if len(self.path):
            norm_path = [
                (
                    x * ctx.size[0] + ctx.posn[0] + ctx.size[0] / 2,
                    y * ctx.size[1] + ctx.posn[1],
                )
                for x, y in self.path
            ]
            pygame.draw.lines(ctx.screen, color, False, norm_path, width)

    def draw_bounds(self, ctx, color=(255, 255, 255), width=1):
        pygame.draw.rect(ctx.screen, color, (ctx.posn, ctx.size), width)

    def draw_maze(self, ctx, color=(100, 100, 100)):
        if self.maze:
            self.maze.draw(ctx, color=color)

    def draw_solve(self, ctx, color=(0, 150, 0)):
        if len(self.solve2) and self.maze:
            for x, y in self.solve2:
                self.maze.draw_cell(ctx, (x, y), color=color)

    def generate(self):
        self.maze = Maze(self.maze_resolution, self.maze_resolution * self.aspect_ratio)

        # Solve an initial path through the maze grid
        start = (self.maze.width // 2, 0)
        end = (self.maze.width // 2, self.maze.height - 1)
        self.solve1 = None

        count = 0
        while self.solve1 is None:
            count += 1
            self.maze.fill_random(
                col_prob=self.maze_density[0], row_prob=self.maze_density[1]
            )
            self.solve1 = bfs(start, end, self.maze.get_neighbors)

            if not self.solve1 and count >= 9999:
                raise Exception("Could not find path (%s tries)" % count)

        # Re-solve over the initial solve but allow diagonal traversal
        grid = []
        for x in range(self.maze.width):
            grid.append([])
            for y in range(self.maze.height):
                if (x, y) in self.solve1:
                    grid[x].append(1)
                else:
                    grid[x].append(0)

        self.solve2 = bfs(start, end, neighbors=lambda cell: grid_neighbors(grid, cell))

        # Interpolate the re-solved path
        # smooth = b_spline(self.solve2, num=self.resolution)
        # self.path = [
        #     (
        #         (x - self.maze_resolution / 2) / self.maze_resolution,
        #         y / (self.maze_resolution * self.aspect_ratio),
        #     )
        #     for x, y in smooth
        # ]

        # self.path[0] = (0, 0)
        # self.path[-1] = (0, 1)

        self.path = [
            (
                (x - self.maze_resolution / 2) / self.maze_resolution,
                y / (self.maze_resolution * self.aspect_ratio),
            )
            for x, y in self.solve2
        ]
