import pygame
import math


def distance_between(start, end):
    x1, y1 = start
    x2, y2 = end

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def angle_between(start, end):
    x1, y1 = start
    x2, y2 = end

    return math.atan2(y2 - y1, x2 - x1)


def follow_path(idx, path, dist):
    if idx == len(path) - 1:
        return path[idx]

    to_next = distance_between(path[idx], path[idx + 1])

    if to_next < dist:
        return follow_path(idx + 1, path, dist - to_next)

    angle = angle_between(path[idx], path[idx + 1])
    x = path[idx][0] + math.cos(angle) * dist
    y = path[idx][1] + math.sin(angle) * dist

    return (x, y)


def calculate_path_length(path):
    length = 0
    for i in range(len(path) - 1):
        curr = path[i]
        next = path[i + 1]
        length += distance_between(curr, next)

    return length


class Growth:
    def __init__(self, path, draw_fidelity=200):
        self.path = path
        self.draw_fidelity = draw_fidelity
        self.reset()

    def reset(self):
        self.length = calculate_path_length(self.path)
        self.progress = 0
        print(self.length)

    def step(self):
        self.progress += 0.01

    def draw(self, ctx, color=(0, 200, 255)):
        draw_distance = self.length * self.progress
        draw_steps = math.floor(draw_distance * self.draw_fidelity)
        draw_increment = draw_distance / draw_steps

        for i in range(draw_steps):
            posn = follow_path(0, self.path, draw_increment * i)
            pygame.draw.circle(ctx.screen, color, ctx.norm(posn), 5)

        # pygame.draw.circle(ctx.screen, color, ctx.norm(self.posn), 5)
