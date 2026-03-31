def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    return a % b

def calc():
    while True:
        print("\n CALC Menu ")
        print("a) Addition")
        print("b) Subtraction")
        print("c) Multiplication")
        print("d) Division")
        print("e) Modulus")
        print("q) Quit")
        
        choice = input("Select an operation").lower()
        
        if choice == 'q':
            break
            
        if choice in ['a', 'b', 'c', 'd', 'e']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 'a':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == 'b':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 'c':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 'd':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == 'e':
                print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
        else:
            print("Invalid")

if _name_ == "_main_":
    calc()
