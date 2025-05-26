#MRO  defines the order in which Python looks for a method or attribute in a hierarchy of multiple inheritance.

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def speak(self):
        print("Mammal makes a sound")

class Bird(Animal):
    def speak(self):
        print("Bird chirps")

class Bat(Mammal):
    def speak(self):
        print("Bat screeches")

class FlyingCreature(Bird):
    def speak(self):
        print("Flying creature flaps and chirps")

# Diamond inheritance: Hybrid inherits from both Bat and FlyingCreature
class Hybrid(Bat, FlyingCreature):
    def info(self):
        print("I am a hybrid creature.")

# Create object of Hybrid
creature = Hybrid()
creature.info()         # Hybrid calls  its own method
creature.speak()        # MRO determines which speak() method to call

# Print full MRO
print("\nMethod Resolution Order:")
for cls in Hybrid.__mro__:
    print(cls.__name__)
