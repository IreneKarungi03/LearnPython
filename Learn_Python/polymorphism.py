class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Function that accepts any animal
def animal_sound(animal):
    animal.speak()

# Create objects
dog = Dog()
cat = Cat()

# Polymorphism in action
animal_sound(dog)   
animal_sound(cat)   
