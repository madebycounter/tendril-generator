import sys
import pygame
from pygame.locals import *
from tendril import Tendril
from growth import Growth
from util.context import DrawContext

pygame.init()
pygame.display.set_caption("Tendril Generator")

size = (800, 600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

tendril = Tendril(
    aspect_ratio=2, resolution=200, maze_resolution=100, maze_density=[0.4, 0.5]
)
tendril.generate()

# growth = Growth(tendril.path)

tendril_size = (size[1] / tendril.aspect_ratio, size[1])
ctx = DrawContext(
    screen,
    posn=((size[0] - tendril_size[0]) / 2, 0),
    size=tendril_size,
)

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_r:
                print("Regenerating...")
                tendril.generate()
                # growth.path = tendril.path
                # growth.reset()

            if event.key == K_p:
                print(tendril.path)

    # growth.step()

    tendril.draw_bounds(ctx)
    tendril.draw_maze(ctx)
    tendril.draw_solve(ctx)
    tendril.draw(ctx)
    # growth.draw(ctx)

    pygame.display.flip()
    clock.tick(30)
