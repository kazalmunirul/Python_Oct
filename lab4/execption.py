# Write a loop that continually asks the user to enter an integer.
# Use a try-except block to handle ValueError if the user enters something that's not a valid integer. Print an informative message.
# The loop should only break when the user successfully enters an integer. Then print the valid integer.

try:
    while True:
    
        user_input = int(input("Enter an integer: "))
        print(user_input)
        break
except ValueError: 
    print("Invalid input. Please enter a valid integer.")  
