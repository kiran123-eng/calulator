 #calcutater to do all calculation
import math
sum=lambda a,b:a+b
subtract=lambda a,b:a-b
multiply=lambda a,b:a*b
square=lambda c:c*c
square_root=lambda a:math.sqrt(a)
division=lambda a,b:a/b if b!=0 else "division with zero is invalid"
def calculator():
    print("Start simple operations")
    print("Operations: +, -, *, /, ** for exponentiation, sqrt for square root")
    #ask user for expression
    while True:  
        expression = input("Enter your expression or type 'exit' to quit: ").strip()

        if expression.lower() == 'exit':  # Exit condition
            print("Exiting calculator. Goodbye!")
            break  # Exit the loop if the user types 'exit'

        try:
            result = eval(expression)
            print(f"The result of {expression} is: {result}")
        except Exception as e:
            print(f"Error: {e}. Please make sure your input is valid.")

# Run the calculator
calculator()

   