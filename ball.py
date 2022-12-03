import pygame
import cfg


class Ball:
    """creates an instance of a ball"""
    IN_PLAY = False
    def __init__(self, window):
        self.window = window
        self.rect = pygame.Rect(162, 150, 20, 20)
        self.x = 0
        self.y = 0
    
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and not Ball.IN_PLAY:
            if event.key == pygame.K_s:
                self.x = 5
                self.y = 5
                Ball.IN_PLAY = True

    def movement(self, objects):
        if Ball.IN_PLAY:
            self.rect.move_ip(self.x, self.y)
            if self.rect.top < 105 or self.rect.bottom > 375:
                self.y = -self.y
            elif self.rect.left < 100 or self.rect.right > 620:
                Ball.IN_PLAY = False
                self.rect.topleft = (162, 150)
            else:
                for object in objects:
                    if self.rect.colliderect(object):
                        self.x = -self.x
                
    def draw(self):
        pygame.draw.rect(self.window, cfg.WHITE, self.rect, 0, border_radius=10)