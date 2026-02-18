#Gavin Waller (2/5/2025)
#This is a comment
catsList = []

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
            
#Test Cat
oCat1 = Cat("Garfield", "male", "Tabby", 5)

#Loop
while True:
    action = input('\nPress I for info, E to eat, M to meow, N to nap, P to play, or Q to quit: ')
    if len(action) > 1:
        action = action[0]  # just use first letter
    action = action.upper()  # force uppercase
    
    if action == 'I':
        oCat1.show()
    elif action == 'E':       
        oCat1.eat()
    elif action == 'M': 
        oCat1.meow()
    elif action == 'N':
        minutes = int(input('How many minutes of nap time? '))
        oCat1.nap(minutes)
    elif action == 'P':
        minutes = int(input('How many minutes of play time? '))
        oCat1.play(minutes)
    elif action == 'Q':
        break
    
print('Bye')