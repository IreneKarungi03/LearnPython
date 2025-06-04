class Person:
    def __init__(self, name, age, gender, national_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.national_id = national_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"National ID: {self.national_id}")


class Student(Person):
    def __init__(self, name, age, gender, national_id, student_id, course, year):
        super().__init__(name, age, gender, national_id)
        self.student_id = student_id
        self.course = course
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")


class Lecturer(Person):
    def __init__(self, name, age, gender, national_id, employee_id, department, specialization):
        super().__init__(name, age, gender, national_id)
        self.employee_id = employee_id
        self.department = department
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Specialization: {self.specialization}")


class Staff(Person):
    def __init__(self, name, age, gender, national_id, staff_id, position, work_area):
        super().__init__(name, age, gender, national_id)
        self.staff_id = staff_id
        self.position = position
        self.work_area = work_area

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Position: {self.position}")
        print(f"Work Area: {self.work_area}")


# Testing the system with sample objects

print("=== Student Info ===")
student = Student("Karungi", 22, "Female", "UG60800067", "S101", "Software Engineering", "Year 3")
student.display_info()

print("\n=== Lecturer Info ===")
lecturer = Lecturer("Dr. Paddy", 46, "Male", "UG4567890", "L200", "Engineering", "Robotics")
lecturer.display_info()

print("\n=== Staff Info ===")
staff = Staff("Shamirah", 38, "Female", "UG3456789", "ST105", "Librarian", "Main Library")
staff.display_info()
