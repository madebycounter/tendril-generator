class DrawContext:
    def __init__(self, screen, posn, size):
        self.screen = screen
        self.posn = posn
        self.size = size

    def norm(self, posn):
        x, y = posn
        return (
            x * self.size[0] + self.posn[0] + self.size[0] / 2,
            y * self.size[1] + self.posn[1],
        )
