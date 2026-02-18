from abc import ABC, abstractmethod

# Abstract Base Class: Person
class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def introduce(self):
        pass

    # Concrete method: shared by all subclasses
    def greet(self):
        return f"Hello! My name is {self._name}."

# Subclass: TennisPlayer
class TennisPlayer(Person):
    def __init__(self, name, age, ranking):
        super().__init__(name, age)
        self._ranking = ranking

    # Implementation of the abstract method
    def introduce(self):
        return f"I'm {self._name}, a {self._age}-year-old tennis player ranked #{self._ranking} in the world."

    # Specific behavior for TennisPlayer
    def play_tennis(self, minutes):
        return f"{self._name} is practicing for {minutes} minutes."

# Subclass: PianoPlayer
class PianoPlayer(Person):
    def __init__(self, name, age, genre):
        super().__init__(name, age)
        self._genre = genre

    # Implementation of the abstract method
    def introduce(self):
        return f"I'm {self._name}, a {self._age}-year-old pianist who specializes in {self._genre} music."

    # Specific behavior for PianoPlayer
    def play_piano(self):
        return f"{self._name} is playing a {self._genre} piece on the piano."

# Example Usage
p1 = TennisPlayer("Coco Gauff", 21, 4)
p2 = PianoPlayer("Billy Joel", 75, "pop")
p3 = TennisPlayer("Carlos Alcaraz", 21, 3)

print(p1.greet())         
print(p1.introduce())     
print(p1.play_tennis(30))   

print(p2.greet())
print(p2.introduce())
print(p2.play_piano())

print(p3.greet())         
print(p3.introduce())     
print(p3.play_tennis(45))   
