# Gavin Waller (2/19/2025)
# This is a comment



# main code/Class code
class Cat():
    def __init__(self, aName, aGender, aBreed, aAge):
        self.name = aName
        self.gender = aGender 
        self.breed = aBreed
        self.energy = 50
        self.hunger = 50
        self.age = aAge
                
    def show(self):
        # example of using formatted strings
        print(f'Cat: {self.name} is a {self.gender} {self.breed}. {self.name} is {self.age} year(s) old.')
        print(f'Energy level: {self.energy}. Hunger level: {self.hunger}.')
        
    def eat(self):
        self.energy = self.energy + 10
        self.hunger = self.hunger - 5
        print(self.name, 'just ate.')
        
    def meow(self):
        self.energy = self.energy - 2
        print(self.name, 'says: Meow!')
        
    def play(self, minutes):
        self.energy = self.energy - (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just played for {minutes} minutes.') 
        
    def nap(self, minutes):
        self.energy = self.energy + (minutes * 2)
        self.hunger = self.hunger + minutes
        print(f'{self.name} just took a {minutes}-minute nap.')
                   
# New class used to organize the process
class AnimalShelter():
    # Setting the Class attributes 
    def __init__(self):
        self.catDict = {}
        self.nextID = 0
        
    #Adding new Cat's to the Dict
    def add(self, name, gender, breed, age):
        
        oCat = Cat(name, gender, breed, age)
        self.catDict[self.nextID] = oCat
        print(f"{name} was added to the shelter, with ID {self.nextID}")
        self.nextID = self.nextID + 1
              
        
    #Display's only one selected Cat    
    def display(self, aNum):
        self.catDict[aNum].show()
        print()
        
        
    #Displays all the Cat    
    def display_all(self):
         for catID in self.catDict:
            print()
            self.catDict[catID].show()         


    
# 
animal_Shelter = AnimalShelter()

#Test Cat
animal_Shelter.add("Garfield", "male", "Tabby", 5)


#Loop
while True:
    action = input('\nPress A add a cat, I for info, D display all cats, or Q to quit: ')
    if len(action) > 1:
        action = action[0]  # just use first letter
    action = action.upper()  # force uppercase
    print()
    
    if action == 'A': # Add new cat
        name = input("What is the cat's name? ")
        gender = input(f"What is {name}'s gender? ")
        breed = input(f"What is {name}'s breed? ")
        age = input(f"How old is {name}? ")
        print()
        animal_Shelter.add(name, gender, breed, age)
        
        

    elif action == 'I': # Shows one cat
        ID = int(input("What is the cat's ID? "))
        animal_Shelter.display(ID)
        print()

    elif action == 'D': # Shows all cats
        animal_Shelter.display_all()
        print()
        
   ### SAVED COMMAND PROMPTS ###     
#     elif action == 'E':       
#         oCat1.eat()
#     elif action == 'M': 
#         oCat1.meow()
#     elif action == 'N':
#         minutes = int(input('How many minutes of nap time? '))
#         oCat1.nap(minutes)
#     elif action == 'P':
#         minutes = int(input('How many minutes of play time? '))
#         oCat1.play(minutes)

    elif action == 'Q':
        break
    
print('Bye')