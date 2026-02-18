# Lab 3

# 1 - Import packages
import pygame, sys, random

# CatImage class - do not change
class CatImage():
    def __init__(self, window):
        self.window = window  # remember the window, so we can draw later
        self.image = pygame.image.load('cat.png') # note the path
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
bounceSound = pygame.mixer.Sound('boing.wav') # note the path



# 5 - Initialize variables
oCat = CatImage(window)
catList = []
catList.append(oCat)  # append the new cat to the list of cats
sound = 0
playSound = 1

    
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
            print("true")
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Press the Green Button
            print(rectangle1Rect.collidepoint(event.pos))
            if rectangle1Rect.collidepoint(event.pos):
                #print("Alive")
                oCat = CatImage(window)
                catList.append(oCat)
            #Press the Red Button
            if rectangle2Rect.collidepoint(event.pos):
                #print("Dead")
                catList.pop()
            #Press the Cats
            for i in range(len(catList)):
                oCat = catList[i]
                if oCat.rect.collidepoint(event.pos):
                    oCat.new_position()

                    
    # 8 - Do any "per frame" actions
        keyPressedTuple = pygame.key.get_pressed()
    if keyPressedTuple[pygame.K_LEFT]:  # moving left
        oCat.x = oCat.x - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_RIGHT]:  # moving right
        oCat.x = oCat.x + N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_UP]:  # moving up
        oCat.y = oCat.y - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_DOWN]:  # moving down
        oCat.y = oCat.y + N_PIXELS_TO_MOVE
        


    #Cat X walls
    if oCat.x >= oCat.maxX:
        oCat.x = oCat.maxX #- 1

        sound += 1
    elif 0 > oCat.x:
        oCat.x = 0

        sound += 1
        #print(sound)

    if oCat.y >= oCat.maxY:
        oCat.y = oCat.maxY #- 1

        sound += 1
        #print(sound)

        
    elif 0 > oCat.y:
        oCat.y = 0

        sound += 1
        
        print(sound)
        
        
    if sound == 1 and playSound == 1:
        bounceSound.play()
        sound = 0
        playSound = 0
    if oCat.x != 0 and oCat.x != oCat.maxX and oCat.y != oCat.maxY and oCat.y != 0:
        #print(sound)
        sound = 0
        playSound = 1


    moveCat = pygame.Rect(oCat.x, oCat.y, 100, 100)
    #TODO ### Check if any keyboard keys are pressed

    # 9 - Clear the window
    window.fill(WHITE)
    
    # 10 - Draw all window elements
    
    #TODO ### Change so that cats do not cover the rectangles' outlines.
    for oCat in catList:
        oCat.draw() 
    rectangle1Rect = pygame.draw.rect(window, GREEN, (150, 400, 100, 50), 3) # 3 pixel edge
    rectangle2Rect = pygame.draw.rect(window, RED, (390, 400, 100, 50), 3) # 3 pixel edge
  
        
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
