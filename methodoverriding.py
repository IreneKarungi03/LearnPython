class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):  # Overriding the method in the parent class
        print("The dog barks")

class Cat(Animal):
    def speak(self):  
        print("The cat meows")
        
class Sheep(Animal):
    def speak(self):
        print("Sheep makes a sound")       

# Test the classes
a = Animal()
a.speak() 

d = Dog()
d.speak()  

c = Cat()
c.speak()  

e = Sheep()
e.speak()
