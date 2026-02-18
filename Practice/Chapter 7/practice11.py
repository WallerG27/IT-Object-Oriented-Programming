# Lab 3

# 1 - Import packages
import pygame, sys, random, pygwidgets

# CatImage class - do not change
class CatImage():
    def __init__(self, window):
        self.window = window  # remember the window, so we can draw later
        self.image = pygame.image.load('images/cat.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.maxX = window.width - self.width
        self.maxY = window.height - self.height
        
        # Pick a random starting position
        self.new_position()
        
    def new_position(self):
        self.x = random.randrange(0, self.maxX)
        self.y = random.randrange(0, self.maxY)

    def get_rect(self):
        return self.rect

    def draw(self):
        self.rect = self.window.blit(self.image, (self.x, self.y))

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_TO_MOVE = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
#bounceSound = pygame.mixer.Sound('boing.wav') # note the path

# 5 - Initialize variables
oCat = CatImage(window)
catList = []
catList.append(oCat)  # append the new cat to the list of cats   

oButtonLeft = pygwidgets.TextButton(window, (150, 400), 'Add Cat', fontSize=28, textColor=(0, 100, 0))      
oButtonRight = pygwidgets.TextButton(window, (390, 400), 'Remove Cat', fontSize=28, textColor=(100, 0, 0))      

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
        
        # See if user clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            for oCat in catList:
                if oCat.get_rect().collidepoint(event.pos):
                    oCat.new_position()
#             if rectangle1Rect.collidepoint(event.pos):
#                 catList.append(CatImage(window))
#             elif rectangle2Rect.collidepoint(event.pos):
#                 if len(catList) > 0:
#                     catList.pop()
#                 else:
#                     bounceSound.play()
    
    if oButtonLeft.handleEvent(event): # When the button is clicked, this returns True
        # the button was clicked, do whatever you want here
        catList.append(CatImage(window))
        if len(catList) == 1:
            oButtonRight.enable()
    if oButtonRight.handleEvent(event):
        catList.pop()
        if len(catList) == 0:
            oButtonRight.disable()
        

    # 8 - Do any "per frame" actions
    # Check for user pressing keys
    keyPressedTuple = pygame.key.get_pressed()
           
    if len(catList) > 0:
        oCat = catList[-1]
        if keyPressedTuple[pygame.K_LEFT]:  # moving left
            if oCat.x == 0:
                #bounceSound.play() # hit border, cannot move
                pass
            elif oCat.x < N_PIXELS_TO_MOVE:
                oCat.x = 0
            else:
                oCat.x = oCat.x - N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_RIGHT]:  # moving right
            if oCat.x == oCat.maxX:
                #bounceSound.play() # hit border, cannot move
                pass
            elif oCat.x > oCat.maxX - N_PIXELS_TO_MOVE:
                oCat.x = oCat.maxX
            else:
                oCat.x = oCat.x + N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_UP]:  # moving up
            if oCat.y == 0:
                #bounceSound.play() # hit border, cannot move
                pass
            elif oCat.y < N_PIXELS_TO_MOVE:
                oCat.y = 0
            else:
                oCat.y = oCat.y - N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_DOWN]:  # moving down
            if oCat.y == oCat.maxY:
                #bounceSound.play() # hit border, cannot move
                pass
            elif oCat.y > oCat.maxY - N_PIXELS_TO_MOVE:
                oCat.y = oCat.maxY
            else:
                oCat.y = oCat.y + N_PIXELS_TO_MOVE            

    # 9 - Clear the window
    window.fill(WHITE)
    
    # 10 - Draw all window elements
    for oCat in catList:
        oCat.draw()   # tell each cat to draw itself
        
#     rectangle1Rect = pygame.draw.rect(window, GREEN, (150, 400, 100, 50), 3) # 3 pixel edge
#     rectangle2Rect = pygame.draw.rect(window, RED, (390, 400, 100, 50), 3) # 3 pixel edge
    
    oButtonLeft.draw()
    oButtonRight.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
