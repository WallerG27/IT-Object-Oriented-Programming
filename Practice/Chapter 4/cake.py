class Bakery:
    def __init__(self):
        self.cakesList = []
    
    def add(self, flavor, price, slices):
        self.cakesList.append(Cake(flavor, price, slices))
        
    def display_all(self):
        for cake in self.cakesList:
            cake.print_description()

    def get_cake(self, flavor):
        for cake in self.cakesList:
            if cake.flavor == flavor:
                return cake
        return None
    
    def get_remaining_slices(self, flavor):
        cake = self.get_cake(flavor)
        if cake:
            return cake.remaining
        else:
            return None
        
    def sell(self, flavor):
        cake = self.get_cake(flavor)
        if cake and cake.remaining >= 1:
            cake.sell(1)                
            return cake.price/cake.slices
        else:
            return None
        
class Cake:
    def __init__(self, flavor, price, slices):
        self.flavor = flavor
        self.price = price
        self.slices = slices
        self.remaining = slices

    def print_description(self):
        print(f"The {self.flavor} cake costs ${self.price} and is divided into {self.slices} slices.")

    def sell(self, count):
        if count <= 0:
            return("Cannot sell zero or negative slices!")
        elif count > self.remaining:
            return(f"Cannot sell more slices than we have ({self.remaining})!")
        else:
            self.remaining -= count
            return f"This cake has {self.remaining} slices remaining."
        
    def getValue(self):
        return (self.price / self.slices) * self.remaining
        
    def isEqualTo(self, otherCake):
        return (self.getValue() == otherCake.getValue())
    
    # Longer version of the above method:
    # def isEqualTo(self, otherCake):
        # myValue = (self.price / self.slices) * self.remaining
        # otherValue = (otherCake.price / otherCake.slices) * otherCake.remaining
        # return (myValue == otherValue)
    
    def isLessThan(self, otherCake):
        return (self.getValue() < otherCake.getValue())
        
    def isGreaterThan(self, otherCake):
        return (self.getValue() > otherCake.getValue())

# Test code for Practice 6
spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)
print(spice_cake.sell(1))
print(chocolate_cake.sell(3))
print("Spice: ", spice_cake.getValue())
print("Spice: ", spice_cake.remaining)
print("Chocolate: ", chocolate_cake.getValue())
print(spice_cake.isEqualTo(chocolate_cake))
print(spice_cake.isGreaterThan(chocolate_cake))
print(spice_cake.isLessThan(chocolate_cake))

# Test code for practice 7
oBakery = Bakery()
oBakery.add("vanilla", 18, 6)
oBakery.add("coconut", 20, 10)

while True:
    action = input('\nPress A to add a cake,'\
                   ' I for info about a cake remaining slices,'\
                   ' P for purchasing a slice of a cake,'\
                   ' D for info about all cakes,'\
                   ' or Q to quit: ')
    if len(action) > 1:
        action = action[0]  # just use first letter
    action = action.upper()  # force uppercase
    
    if action == 'A':
        f = input("New cake: what is the flavor? ")
        p = int(input("What is the price for the whole cake?"))
        s = int(input("How many slices are in the cake?"))
        oBakery.add(f, p, s)
        print("Cake added.")
    elif action == 'I':
        f = input("Cake info: what flavor? ")
        numSlices = oBakery.get_remaining_slices(f)
        if numSlices:
            print(f"The {f} cake has {numSlices} slices remaining.")
        else:
            print("Cake not found.")
    elif action == 'P':
        f = input("Buy slice: what flavor? ")
        price = oBakery.sell(f)
        if price:
            print(f"A slice of the {f} cake costs ${price}.")
        else:
            print(f"There are no slices of the {f} cake.")
    elif action == 'D':
        oBakery.display_all()
    elif action == 'Q':
        break
