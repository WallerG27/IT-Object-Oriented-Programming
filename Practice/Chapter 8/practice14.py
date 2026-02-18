class Animal:
    kingdom = "Animalia"
    
    def __init__(self, name):
        self.name = name
        

a1 = Animal('Pluto')
a2 = Animal('Goofy')
print(a1.name, a1.kingdom)
print(a2.name, a2.kingdom)
print(Animal.kingdom)


class Car:
    wheels = 4
c1 = Car()
c2 = Car()

print(c1.wheels)
print(c2.wheels)
print(Car.wheels)

Car.wheels = 6

c3 = Car()

print(c1.wheels)
print(c2.wheels)
print(c3.wheels)
print(Car.wheels)

c1.wheels = 8


print(c1.wheels)
print(c2.wheels)
print(c3.wheels)
print(Car.wheels)


class Person:
    species = 'Homo Sapiens'
    person_count = 0
    def __init__(self, name):
        Person.person_count += 1
        self.name = name
        
        
        def __del__(self):
            Person.person_count -= 1
            
            
class Student(Person):
    courses = ['2512', '2513', '1540']
    
p1 = Person("Bass")

p2 = Person("Mary")

p3 = Student("Gavin")
Student.species = 'Barely Homo Sapiens'

p4 = Student("John")

print(p1.name, Person.species)
print(p2.name, Person.species)
print(p3.name, Student.species)
print(p4.name, Student.species)
p3.courses.append('3515')

print(p3.name, p3.courses)
print(p4.name, p4.courses)
print(Student.courses)
