# 1 - Import packages and define classes
import pygame, pygwidgets, sys

class Cat():
    def __init__(self, name, gender, breed, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.energy = 50
        self.hunger = 50
    
    def show(self):
        print(f'Cat: {self.name} is a {self.gender} {self.breed}. '\
              f'{self.name} is {self.age} year(s) old.')        
        print(f'Energy level: {self.energy}.'\
              f' Hunger level: {self.hunger}.\n')
    
    def eat(self):
        self.energy += 10
        self.hunger -= 5
        print(self.name, 'just ate.')
        
    def meow(self):
        self.energy -= 2
        print(self.name, 'says: Meow!')
        
    def play(self, minutes):
        self.energy -= (minutes * 2)
        self.hunger += minutes
        print(f'{self.name} just played for {minutes} minutes.') 
        
    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.') 

class AnimalShelter():
    def __init__(self):
        self.animalDict = {}
        self.nextId = 0

    def add(self, name, gender, breed, age):
        self.animalDict[self.nextId] = Cat(name, gender, breed, age)
        self.nextId += 1
        return self.nextId-1
    
    def display(self, aNum):
        self.animalDict[aNum].show()
        
    def display_all(self):
        for animal in self.animalDict.values():
            animal.show()

# main code

# 2 - Define constants
BLACK = (0, 0, 0)
BACKGROUND = (25, 64, 88) #Dark Blue
TEXT_COLOR = (235, 129, 55) #Orange
FOCUS_COLOR = (255, 55, 0) #Red
TL = 70 # TEXT_LOCATION
IL = 170 # INPUT_LOCATION
UP_COLOR = (210, 220, 220) #Dull White/Blue
OVER_COLOR = (255, 207, 135) #Yellow-Orange (255, 255, 55)
BUTTON_DOWN = (171, 219, 227) # Cyan

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
# None

# 5 - Initialize variables
### TEXT ### 
oTitle = pygwidgets.DisplayText(window, (25, 30), 'Add a Cat to the Shelter', fontSize=36, textColor=TEXT_COLOR) 
oNameText = pygwidgets.DisplayText(window, (TL, 70), 'Name:', fontSize=32, textColor=TEXT_COLOR, justified='center')
oGenderText = pygwidgets.DisplayText(window, (TL, 100), 'Gender:', fontSize=32, textColor=TEXT_COLOR, justified='center')
oBreedText = pygwidgets.DisplayText(window, (TL, 130), 'Breed:', fontSize=32, textColor=TEXT_COLOR, justified='center') 
oAgeText = pygwidgets.DisplayText(window, (TL, 160), 'Age:', fontSize=32, textColor=TEXT_COLOR, justified='center')
oInputText = pygwidgets.DisplayText(window, (20, 270), 'All Fields are required.', fontSize=36, textColor=TEXT_COLOR, justified='right')

### INFORMATION FIELDS ###
#Text Inputs
oNameInput = pygwidgets.InputText(window, (IL, 70), fontName=None, fontSize=32, width=200, focusColor=FOCUS_COLOR, textColor=TEXT_COLOR, initialFocus = True)
oBreedInput = pygwidgets.InputText(window, (IL, 130), fontName=None, fontSize=32, width=200, focusColor=FOCUS_COLOR, textColor=TEXT_COLOR)
oAgeInput = pygwidgets.InputText(window, (IL, 160), fontName=None, fontSize=32, width=30, focusColor=FOCUS_COLOR, textColor=TEXT_COLOR)
#Radio Buttons
oRadioFemale = pygwidgets.TextRadioButton(window, (170, 100), 'GenderGroup', 'Female', nickname='Female') 
oRadioMale = pygwidgets.TextRadioButton(window, (245, 100), 'GenderGroup', 'Male', nickname='Male') 
oRadioOther = pygwidgets.TextRadioButton(window, (300, 100), 'GenderGroup', 'Unknown', value = True, nickname='Unknown')

### Buttons ###
oAddButton = pygwidgets.TextButton(window, (250, 200), 'Add', fontSize=32, textColor=TEXT_COLOR, upColor=UP_COLOR, overColor=OVER_COLOR, downColor=BUTTON_DOWN, enterToActivate=True)
oShowAllButton = pygwidgets.TextButton(window, (370, 420), 'Show all cats (in shell)', fontSize=32, textColor=TEXT_COLOR, upColor=UP_COLOR, overColor=OVER_COLOR, downColor=BUTTON_DOWN, enterToActivate=True)

# Manually add the first cat, Garfield, to the shelter
oAnimalShelter = AnimalShelter()
newId = oAnimalShelter.add('Garfield', 'male', 'Tabby', 5)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
            
        inputGender = oRadioOther.getSelectedRadioButton()
        if oRadioFemale.handleEvent(event): # When clicked on to select, this returns True
            pass
            # RadioButton was clicked, do whatever you want here
        if oRadioMale.handleEvent(event): # When clicked on to select, this returns True
            pass
        
        if oRadioOther.handleEvent(event): # When clicked on to select, this returns True
            pass
        
        
        
        oNameInput.handleEvent(event)
        oBreedInput.handleEvent(event)
        oAgeInput.handleEvent(event)
        
        if (oAddButton.handleEvent(event)):
            error = False
            errorLyst = []
            catName = oNameInput.getValue()
            catBreed = oBreedInput.getValue()
            catAge = oAgeInput.getValue()
            if catName == '':
                errorLyst.append("Name is Required")
                error = True
                
            if catBreed == '':
                errorLyst.append("Breed is Required")
                error = True
                
            if catAge == '':
                errorLyst.append("Age is Required (Integer)")
                error = True
            else:
                try:
                    int(catAge)
                except:
                    error = True
                    errorLyst.append("Age must be an Integer")
                else:
                    pass
                

            if error == True:
                oInputText = pygwidgets.DisplayText(window, (20, 270), '', fontSize=36, textColor=FOCUS_COLOR, justified='right') 
                oInputText.setValue('Double Check: ' + "\n-".join(errorLyst))
            else:

                newId = oAnimalShelter.add(catName, inputGender, catBreed, catAge)
                
                oInputText = pygwidgets.DisplayText(window, (20, 270), '', fontSize=36, textColor=TEXT_COLOR, justified='left') 
                oInputText.setValue(catName + ' has been added with the Id Number: ' + str(newId))
                #Removes text and focus
                oNameInput.clearText(True)
                oBreedInput.clearText(True)
                oBreedInput.removeFocus()
                oAgeInput.clearText(True)
                oAgeInput.removeFocus()
        
        if (oShowAllButton.handleEvent(event)):
            oAnimalShelter.display_all()


    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BACKGROUND)
    
    # 10 - Draw all window elements
    ### TEXT ###
    oTitle.draw()
    oNameText.draw()
    oGenderText.draw()
    oBreedText.draw()
    oAgeText.draw()
    oInputText.draw()
    ### INFORMATION FIELDS ###
    #Text Inputs
    oNameInput.draw()
    oBreedInput.draw()
    oAgeInput.draw()
    #Radio Buttons
    oRadioFemale.draw()
    oRadioMale.draw()
    oRadioOther.draw()
    
    ### Buttons ###
    oAddButton.draw()
    oShowAllButton.draw()

    

    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
