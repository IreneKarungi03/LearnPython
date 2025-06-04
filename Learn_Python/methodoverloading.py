class Calculator:
    def add(self, *numbers): # *numbers allows the method to accept any number of arguments.
        total = 0
        for num in numbers: #This is a loop that goes through each value in the numbers collection.
            total += num
        return total

    def multiply(self, *numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    def average(self, *numbers):
        if len(numbers) == 0:
            return 0
        return self.add(*numbers) / len(numbers)

    


# Create an object of Calculator
calc = Calculator()

# Test cases
print("Addition:")
print("2 + 3 =", calc.add(2, 3))
print("1 + 2 + 3 + 4 + 5 =", calc.add(1, 2, 3, 4, 5))

print("\nMultiplication:")
print("2 * 3 =", calc.multiply(2, 3))
print("2 * 3 * 4 =", calc.multiply(2, 3, 4))

print("\nAverage:")
print("Average of 10, 20, 30 =", calc.average(10, 20, 30))
print("Average of no numbers =", calc.average())


