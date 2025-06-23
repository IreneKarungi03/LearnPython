class Car:
    def __init__(self, brand, model, year):
        self.brand = brand      
        self.model = model      
        self.year = year        

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2019)
car2 = Car("Honda", "Accord", 2017)

# Using object methods
car1.display_info()   
car2.display_info()  
