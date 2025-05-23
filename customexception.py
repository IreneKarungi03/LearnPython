# Define custom exception
class NotPositiveError(Exception):
    def __init__(self, value):
        super().__init__(f"Invalid input: {value} is not a positive number")

# Function to check for a positive number
def check_positive(number):
    if number <= 0:
        raise NotPositiveError(number)
    else:
        print(f"{number} is a positive number.")

# an exception example9

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
except NotPositiveError as e:
    print(e)
except ValueError:
    print("Invalid input: please enter a number.")
