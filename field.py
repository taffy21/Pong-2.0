import pygame
import cfg

class Field:
    """creates an instance of a field"""

    def __init__(self, window):
        self.window = window
        self.color = cfg.TEAL
        self.rect = pygame.Rect(100, 100, 520, 280)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        pygame.draw.rect(self.window, cfg.WHITE, self.rect, 5)
        pygame.draw.line(self.window, cfg.WHITE, (360, 100), (360, 380), 5)
        pygame.draw.line(self.window, cfg.WHITE, (155, 100), (155, 380), 5)
        pygame.draw.line(self.window, cfg.WHITE, (565, 100), (565, 380), 5)
