# Basic Calculator in Python

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers. Handle division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def get_numbers():
    """Prompt the user to input two numbers."""
    print("Enter two numbers:")
    num1 = input("First number: ")
    num2 = input("Second number: ")
    if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
        return float(num1), float(num2)
    else:
        return None, None

def calculator():
    """Main calculator function to interact with the user."""
    while True:
        print("\nWelcome to the Python Calculator!")
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter the number corresponding to your choice (1-5): ")
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "Division"

            print(f"The result of {operation} is: {result}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid operation.")

# Call the calculator function directly
calculator()
