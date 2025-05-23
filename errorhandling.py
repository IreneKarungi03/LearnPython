while True:
    try:
        # Ask for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Attempt the division
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
        break  # Exit the loop if successful

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a non-zero second number.")
