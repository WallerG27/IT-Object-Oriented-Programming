# 1 - Import packages and define classes
import pygame, pygwidgets, sys
from abc import ABC, abstractmethod

class AnimalShelter():
    def __init__(self):
        self.animalDict = {}
        self.nextId = 0

    def add(self, name, gender, breed, age, pet_type):
        if pet_type == 'Cat':
            self.animalDict[self.nextId] = Cat(name, gender, breed, age)
        if pet_type == 'Dog':    
            self.animalDict[self.nextId] = Dog(name, gender, breed, age)
        if pet_type == 'Fish':
            self.animalDict[self.nextId] = Fish(name, gender)
            
        self.nextId += 1
        return self.nextId-1
    
    def display(self, aNum):
        self.animalDict[aNum].show()
        
    def display_all(self):
        for animal in self.animalDict.values():
            animal.show()

    def feed_all(self):
        for animal in self.animalDict.values():
            animal.eat()
            
    def speak_all(self):
        for animal in self.animalDict.values():
            animal.speak()
            
            
#The Alphabet makes it abstract
class Animal(ABC):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.hunger = 50
        self.energy = 50


    def eat(self):
        self.energy += 10
        self.hunger -= 5
        print(self.name, 'just ate.\n')    
        
    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.')
        
    def play(self, minutes):
        self.energy -= (minutes * 2)
        self.hunger += minutes
        print(f'{self.name} just played for {minutes} minutes.') 
        
    
    @abstractmethod
    def speak(self):
        pass
    
    
    
class Cat(Animal):
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
        
    def speak(self):
        self.energy -= 2
        print(self.name, 'says: Meow!\n') 
    
 
 
 
class Dog(Animal):
    def __init__(self, name, gender, breed, age):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.energy = 50
        self.hunger = 50
    
    def show(self):
        print(f'Dog: {self.name} is a {self.gender} {self.breed}. '\
              f'{self.name} is {self.age} year(s) old.')        
        print(f'Energy level: {self.energy}.'\
              f' Hunger level: {self.hunger}.\n')
        
    def speak(self):
        self.energy -= 2
        print(self.name, 'says: woof!\n')




class Fish(Animal):

    
    def show(self):
        print(f'Fish: {self.name} is a {self.gender}.')        
        print(f'Energy level: {self.energy}.'\
              f' Hunger level: {self.hunger}.\n')
        
    def speak(self):
        self.energy -= 2
        print(self.name, 'says: glub!\n')










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
oTypeText = pygwidgets.DisplayText(window, (TL, 70), 'Type:', fontSize=32, textColor=TEXT_COLOR, justified='center')
oNameText = pygwidgets.DisplayText(window, (TL, 100), 'Name:', fontSize=32, textColor=TEXT_COLOR, justified='center')
oGenderText = pygwidgets.DisplayText(window, (TL, 130), 'Gender:', fontSize=32, textColor=TEXT_COLOR, justified='center')
oBreedText = pygwidgets.DisplayText(window, (TL, 160), 'Breed:', fontSize=32, textColor=TEXT_COLOR, justified='center') 
oAgeText = pygwidgets.DisplayText(window, (TL, 190), 'Age:', fontSize=32, textColor=TEXT_COLOR, justified='center')
oInputText = pygwidgets.DisplayText(window, (20, 240), 'All Fields are required.', fontSize=36, textColor=TEXT_COLOR, justified='right')

### INFORMATION FIELDS ###
#Text Inputs
oNameInput = pygwidgets.InputText(window, (IL, 100), fontName=None, fontSize=32, width=200, focusColor=FOCUS_COLOR, textColor=TEXT_COLOR, initialFocus = True)
oBreedInput = pygwidgets.InputText(window, (IL, 160), fontName=None, fontSize=32, width=200, focusColor=FOCUS_COLOR, textColor=TEXT_COLOR)
oAgeInput = pygwidgets.InputText(window, (IL, 190), fontName=None, fontSize=32, width=30, focusColor=FOCUS_COLOR, textColor=TEXT_COLOR)

##Radio Buttons
#Animal Type
oRadioCat = pygwidgets.TextRadioButton(window, (170, 70), 'AnimalType', 'Cat', nickname='Cat') 
oRadioDog = pygwidgets.TextRadioButton(window, (225, 70), 'AnimalType', 'Dog', nickname='Dog') 
oRadioFish = pygwidgets.TextRadioButton(window, (280, 70), 'AnimalType', 'Fish', value = True, nickname='Fish')
#Gender
oRadioFemale = pygwidgets.TextRadioButton(window, (170, 130), 'GenderGroup', 'Female', nickname='Female') 
oRadioMale = pygwidgets.TextRadioButton(window, (245, 130), 'GenderGroup', 'Male', nickname='Male') 
oRadioOther = pygwidgets.TextRadioButton(window, (300, 130), 'GenderGroup', 'Unknown', value = True, nickname='Unknown')

### Buttons ###
oAddButton = pygwidgets.TextButton(window, (250, 340), 'Add', fontSize=32, textColor=TEXT_COLOR, upColor=UP_COLOR, overColor=OVER_COLOR, downColor=BUTTON_DOWN, enterToActivate=True)
oFeedAllButton = pygwidgets.TextButton(window, (TL, 420), 'Feed All', fontSize=32, textColor=TEXT_COLOR, upColor=UP_COLOR, overColor=OVER_COLOR, downColor=BUTTON_DOWN, enterToActivate=True)
oSpeakAllButton = pygwidgets.TextButton(window, (200, 420), 'Speak All', fontSize=32, textColor=TEXT_COLOR, upColor=UP_COLOR, overColor=OVER_COLOR, downColor=BUTTON_DOWN, enterToActivate=True)
oShowAllButton = pygwidgets.TextButton(window, (340, 420), 'Show all (in shell)', fontSize=32, textColor=TEXT_COLOR, upColor=UP_COLOR, overColor=OVER_COLOR, downColor=BUTTON_DOWN, enterToActivate=True)

# Manually add the first cat, Garfield, to the shelter
oAnimalShelter = AnimalShelter()
newId = oAnimalShelter.add('Garfield', 'male', 'Tabby', 5, Cat)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
            
        AnimType = oRadioFish.getSelectedRadioButton()
        if oRadioCat.handleEvent(event): # When clicked on to select, this returns True
            pass
            # RadioButton was clicked, do whatever you want here
        if oRadioDog.handleEvent(event): # When clicked on to select, this returns True
            pass
        
        if oRadioFish.handleEvent(event): # When clicked on to select, this returns True
            pass            
            
        if AnimType != 'Fish':
            oBreedText.show()
            oAgeText.show()
            oBreedInput.show()
            oAgeInput.show()
        else:
            oBreedText.hide()
            oAgeText.hide()
            oBreedInput.hide()
            oAgeInput.hide()
            
            
            
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
            name = oNameInput.getValue()
            breed = oBreedInput.getValue()
            age = oAgeInput.getValue()

            if name == '':
                errorLyst.append("Name is Required")
                error = True
            if AnimType != 'Fish':
                if breed == '':
                    errorLyst.append("Breed is Required")
                    error = True
                    
                if age == '':
                    errorLyst.append("Age is Required (Integer)")
                    error = True
                else:
                    try:
                        int(age)
                    except:
                        error = True
                        errorLyst.append("Age must be an Integer")
                    else:
                        pass
                
            
            if error == True:
                oInputText = pygwidgets.DisplayText(window, (20, 240), '', fontSize=36, textColor=FOCUS_COLOR, justified='right') 
                oInputText.setValue('Double Check: ' + "\n-".join(errorLyst))
            else:

                newId = oAnimalShelter.add(name, inputGender, breed, age, AnimType)
                
                oInputText = pygwidgets.DisplayText(window, (20, 270), '', fontSize=36, textColor=TEXT_COLOR, justified='left') 
                oInputText.setValue(name + ' has been added with the Id Number: ' + str(newId))
                #Removes text and focus
                oNameInput.clearText(True)
                oBreedInput.clearText(True)
                oBreedInput.removeFocus()
                oAgeInput.clearText(True)
                oAgeInput.removeFocus()
                
        if (oFeedAllButton.handleEvent(event)):
            oAnimalShelter.feed_all()
        
        if (oSpeakAllButton.handleEvent(event)):
            oAnimalShelter.speak_all()
            
        if (oShowAllButton.handleEvent(event)):
            oAnimalShelter.display_all()


    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BACKGROUND)
    
    # 10 - Draw all window elements
    ### TEXT ###
    oTitle.draw()
    oTypeText.draw()
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
    ##Radio Buttons
    #Animal Type
    oRadioCat.draw()
    oRadioDog.draw()
    oRadioFish.draw()
    #Gender
    oRadioFemale.draw()
    oRadioMale.draw()
    oRadioOther.draw()
    
    ### Buttons ###
    oAddButton.draw()
    oFeedAllButton.draw()
    oSpeakAllButton.draw()
    oShowAllButton.draw()

    

    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
