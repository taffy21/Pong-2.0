import pygame
import sys
import cfg
import screens
import pygwidgets
import field
import players
import ball

#initialisations
pygame.init()
window = pygame.display.set_mode(cfg.SIZE)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# assets

# variables
player_score = 0
computer_score = 0
my_score = pygwidgets.DisplayText(window, (100, 20), f"PLAYER SCORE: {player_score}", "Arial", 24, textColor=cfg.WHITE)
comp_score = pygwidgets.DisplayText(window, (400, 20), f"COMPUTER SCORE: {computer_score}", "Arial", 24, textColor=cfg.WHITE)

#this is code to just make the game work :)
re_adjusted_player = 0
re_adjusted_comp = 0


my_field = field.Field(window)

# may have to separate non-updating vs updating score

my_player = players.Player(window)
comp_player = players.Computer(window)
my_ball = ball.Ball(window)

def startScreen():
    "function to draw the players and ball on the field"
    my_player.draw()
    comp_player.draw()
    my_ball.draw()
    
def allMovements():
    """all player movements"""
    my_player.movement()  
    comp_player.movement()    
    my_ball.movement([comp_player.rect, my_player.rect])


firstScreen = screens.ScreenOne(window)
thirdScreen = screens.ScreenThree(window)
state = "Opening"

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
        if firstScreen.handleEvent(event):
            state = "Second"

        if my_player.handleEvent(event):
            pass

        if my_ball.handleEvent(event):
            pass
    
    window.fill(cfg.BLACK)

    if state == "Opening":
        firstScreen.draw()
    
    if state == "Second":
        my_field.draw()
        my_score.draw()
        comp_score.draw()

        startScreen()  
                    
        allMovements()
        if my_ball.rect.left <= 120:
            computer_score += 1
            re_adjusted_comp = int(computer_score/4) # if it works, fix it later :D
            comp_score.setValue(f"COMPUTER SCORE: {re_adjusted_comp}")
                
        elif my_ball.rect.right >= 600:
            player_score += 1
            re_adjusted_player = int(player_score/4) # if it works, fix it later :D
            my_score.setValue(f"PLAYER SCORE: {re_adjusted_player}")

        
        if re_adjusted_player == 5 or re_adjusted_comp == 5:
            state = "Third"

    if state == "Third":
        thirdScreen.draw()
        
    pygame.display.update()

    clock.tick(cfg.FRAMES_PER_SEC)

