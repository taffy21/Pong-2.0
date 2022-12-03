import pygame
import cfg

class ScreenOne:
    """opening screen"""   

    def __init__(self, window):
        pygame.font.init()        
        self.window = window
        self.font = pygame.font.SysFont("Arial", 28)

        self.ftext = self.font.render("Pong 2.0: First to Five Edition", False, cfg.WHITE)
        self.frect = self.ftext.get_rect(topleft = (250, 100))

        self.stext = self.font.render("Press Play to Start!!", False, cfg.WHITE)
        self.srect = self.stext.get_rect(topleft = (280, 200))

        self.playbutton = self.font.render("Play", False, cfg.WHITE)
        self.prect = self.playbutton.get_rect(topleft = (335, 300))  

    def handleEvent(self, event):        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.prect.collidepoint(event.pos):
                return True
                    
    def draw(self):
        self.window.blit(self.ftext, self.frect)
        self.window.blit(self.stext, self.srect)
        pygame.draw.rect(self.window, cfg.GREY, self.prect, 0)
        self.window.blit(self.playbutton, self.prect)


class ScreenTwo:
    """playing screen"""
    def __init__(self, window):
        pass


class ScreenThree:
    """last screen"""
    def __init__(self, window):
        pygame.font.init()        
        self.window = window
        self.font = pygame.font.SysFont("Arial", 28)

        self.gtext = self.font.render("GAME OVER", False, cfg.WHITE)
        self.grect = self.gtext.get_rect(topleft = (250, 100))

        self.playbutton = self.font.render("Play", False, cfg.WHITE)
        self.prect = self.playbutton.get_rect(topleft = (335, 300))  

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.prect.collidepoint(event.pos):
                pass
                    
    def draw(self):
        self.window.blit(self.gtext, self.grect)
        


