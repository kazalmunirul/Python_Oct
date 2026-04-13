
try:
    a = 10
    b_str = input("Enter a number to divide by: ")
    b = int(b_str)  # Can raise ValueError
    c = a / b       # Can raise ZeroDivisionError
    print(f"Result: {c}")
except ValueError:
    print("Invalid input. Please enter a valid number..")
except ZeroDivisionError:
   print("cannot divide by zero. ")
except Exception as e:
        print(f"An error occurred: {e} \n , Please contact developer.")





