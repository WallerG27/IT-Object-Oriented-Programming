# 1 - Import packages
import pygame, sys, random

# Ball class 
class Ball():
    def __init__(self, window):
        self.window = window  # remember the window, so we can draw later
        self.image = pygame.image.load('images/ball.png')

        # A rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = window.width - self.width
        self.maxHeight = window.height - self.height
        
        # Pick a random starting position 
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)
        
    def change_position(self):
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
  # The image is now being retrieved in the Ball class
  
# 5 - Initialize variables
oBall = Ball(window)
ballList = []
ballList.append(oBall)  # append the first ball to the list of balls   

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
            
        # TODO
        # Hint: look at the available methods in the Ball class.
        # Check if a mouse down event happened
            # If the mouse click was on a ball
                # Change the position of the clicked ball
            # If the mouse click was on the rectangle
                # Add a new ball
        

    # 8 - Do any "per frame" actions
  
    # 9 - Clear the window
    window.fill(WHITE)
    
    # 10 - Draw all window elements
    rectangleRect = pygame.draw.rect(window, BLACK, (400, 300, 100, 50), 3) # 3 pixel edge

    # TODO: every ball needs to be drawn (not just one).
    oBall.draw() # tell a ball to draw itself
    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

