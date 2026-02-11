# Basic Calculator using input

class Calculator:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            raise ValueError("Division by zero is not allowed")
        
    def square(self):
        if self.num1 >=0:
            return self.num1 ** self.num2
        else:
            raise ValueError("Square of negative number is not allowed")

# Choosing Operation
operation = input("Enter operation (+, -, *, /, square): ")
# Accepting user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the Second number: "))

# Creating a Calculator instance
calculator = Calculator(num1, num2)

operations = {
    '+': calculator.add,
    '-': calculator.subtract,
    '*': calculator.multiply,
    '/': calculator.divide,
    'square': calculator.square
}

if operation in operations:
    try:
        result = operations[operation]()
        print(f"The result is: {result}")
    except ValueError as e:
        print(e)

else:
    print("Invalid operation")