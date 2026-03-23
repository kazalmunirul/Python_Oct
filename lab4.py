# Ask the user to enter two numbers.
# Ask the user to enter an operation (+, -, *, /).Based on the operation, 
# calculate and print the result.
num1    = float(input("Enter 1st value "))
num2    = float(input("Enter 2nd value "))
operation = input("enter operation (+, -, *, /) ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation")  
print("Result:", result)

    

