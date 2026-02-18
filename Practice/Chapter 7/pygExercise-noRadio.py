# Practice 12 - PARTIAL solution
# Homework: Add radio buttons
# Does not need to be submitted BUT you are expected to finish it before Lab 4.

# 1 - Import packages
import pygame, sys, random, pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
DARK_BLUE = (51, 51, 151)
LIGHT_YELLOW = (255, 255, 204)
RED = (255, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables

oMessageTextA = pygwidgets.DisplayText(window, (20, 50), 'Enter your name: ', 
                                    fontSize=36, textColor=BLACK)

oUserInputA = pygwidgets.InputText(window, (250, 55), '', focusColor=RED,
                                   fontSize=36, textColor=DARK_BLUE,
                                   backgroundColor=WHITE, initialFocus=True)

oSubmitButton = pygwidgets.TextButton(window, (240, 155), 'Submit', fontSize=32,
                                      textColor=DARK_BLUE, enterToActivate=True)

oMessageTextB = pygwidgets.DisplayText(window, (20, 250),
                                       'Hello!', 
                                       fontSize=36, textColor=DARK_BLUE,
                                       justified='center')

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        oUserInputA.handleEvent(event)

        if (oSubmitButton.handleEvent(event)): 
            userText = oUserInputA.getValue()
            #userText = oUserInputA.text # do not do this
            
            oMessageTextB.setValue('Hello ' + userText + '! ')
            oUserInputA.clearText(True)
            
    # 8 - Do any "per frame" actions


    # 9 - Clear the window before drawing it again
    window.fill(LIGHT_YELLOW)
                          
    # 10 - Draw the window elements

    oMessageTextA.draw()
    oUserInputA.draw()
    oSubmitButton.draw()
    
    oMessageTextB.draw()
    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
