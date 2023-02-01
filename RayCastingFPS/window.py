import pygame

pygame.init()


class Window:
    def __init__(self, fps: int = 30, name: str = "Ray casting FPS"):
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.window = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.fps = fps
        self.frame = -1
        self.clock = pygame.time.Clock()
        self.name = name
        self.run = True

        self.setup()

    def setup(self):
        pygame.display.set_caption(self.name)

    def update_caption(self, caption: str = None):
        if caption is None:
            caption = self.name

        pygame.display.set_caption(caption)
