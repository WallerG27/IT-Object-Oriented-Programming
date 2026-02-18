
def show():
    global name, gender, breed, energy, hunger, age
    # example of using formatted strings
    print(f'Cat: {name} is a {gender} {breed}. {name} is {age} year(s) old.')
    print(f'Energy level: {energy}. Hunger level: {hunger}.')
    
def eat():
    global name, energy, hunger
    energy = energy + 10
    hunger = hunger - 5
    print(name, 'just ate.')
    
def meow():
    global name, energy
    energy = energy - 2
    print(name, 'says: Meow!')
    
def play(minutes):
    global name, energy, hunger
    energy = energy - (minutes * 2)
    hunger = hunger + minutes
    print(f'{name} just played for {minutes} minutes.') 
    
def nap(minutes):
    global name, energy, hunger
    energy = energy + (minutes * 2)
    hunger = hunger + minutes
    print(f'{name} just took a {minutes}-minute nap.') 
    
# main code

name = "Garfield"
gender = "male"
breed = "Tabby"
energy = 50
hunger = 50
age = 5

while True:
    action = input('\nPress I for info, E to eat, M to meow, N to nap, P to play, or Q to quit: ')
    if len(action) > 1:
        action = action[0]  # just use first letter
    action = action.upper()  # force uppercase
    
    if action == 'I':
        show()
    elif action == 'E':       
        eat()
    elif action == 'M': 
        meow()
    elif action == 'N':
        minutes = int(input('How many minutes of nap time? '))
        nap(minutes)
    elif action == 'P':
        minutes = int(input('How many minutes of play time? '))
        play(minutes)
    elif action == 'Q':
        break
    
print('Bye')
    
    
    
