# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random, pygwidgets


# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables
nameText = pygwidgets.DisplayText(window, (20, 50), 'Enter your name:', fontSize=28, textColor=(0, 0, 0))      
major = pygwidgets.DisplayText(window, (90, 100), 'Pick a major', fontSize=28, textColor=(0, 0, 0))      
nameInput = pygwidgets.InputText(window, (240, 50), fontName=None, fontSize=28, width=200, textColor=(0, 0, 0))
radioIT = pygwidgets.TextRadioButton(window, (240, 100), 'buttonsGroup', 'it') 
radioCyS = pygwidgets.TextRadioButton(window, (290, 100), 'buttonsGroup', 'CyS') 
radioOther = pygwidgets.TextRadioButton(window, (340, 100), 'buttonsGroup', 'Others') 
submit = pygwidgets.TextButton(window, (200, 200), 'submit', fontSize=28, textColor=(0, 100, 0))      
 
# 6 - Loop forever
while True:
    random1 = random.randrange(-3, 1)
    random2 = random.randrange(-1, 3)
    random3 = random.randrange(-3, 1)
    BACKGROUND = ((50 + random1), (100 + random2), (200 + random3))
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
        
        if nameInput.handleEvent(event):
            theText = nameInput.getValue() # call this method to get the text the user typed in the field # Do whatever you want with theText
        
        if radioIT.handleEvent(event): # When clicked on to select, this returns True
            pass
            # RadioButton was clicked, do whatever you want here
        if radioCyS.handleEvent(event): # When clicked on to select, this returns True
            pass
        
        if radioOther.handleEvent(event): # When clicked on to select, this returns True
            pass
        
        
        if submit.handleEvent(event): # When the button is clicked, this returns True
        # the button was clicked, do whatever you want here
            if thetext != null:
                print(theText + " gets 5 big booms")
            
    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BACKGROUND)
    
    # 10 - Draw all window elements
    nameText.draw()
    major.draw()
    nameInput.draw()
    radioIT.draw()
    radioCyS.draw()
    radioOther.draw()
    submit.draw()
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
