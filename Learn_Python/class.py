 # Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Subclass Student inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

# Subclass Lecturer inherits from Person
class Lecturer(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
        
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

student = Student("Rutebuuka", 25, "S123")
lecturer = Lecturer("Dr. Emmanuel", 39, "E456")

student.display_info()
print("---")
lecturer.display_info()
