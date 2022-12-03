import pygame
import cfg

class Player:
    """creates an instance of a player"""
    def __init__(self, window):
        self.window = window
        self.rect = pygame.Rect(150, 105, 12, 100)
        self.y = 0

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:                   
                self.y = -5                              
            if event.key == pygame.K_m:
                self.y = 5              
    
    def movement(self):
        self.rect.move_ip(0, self.y)
        if self.rect.top < 105 or self.rect.bottom > 375:
            self.y = 0

    def draw(self):
        pygame.draw.rect(self.window, cfg.BROWN, self.rect)

class Computer:
    """creates an instance of a computer"""
    def __init__(self, window):
        self.window = window
        self.rect = pygame.Rect(560, 105, 12, 100)
        self.y = 8

    def movement(self):
        self.rect.move_ip(0, self.y)
        if self.rect.top < 105 or self.rect.bottom > 375:
            self.y =-self.y
            
    def draw(self):
        pygame.draw.rect(self.window, cfg.BROWN, self.rect)