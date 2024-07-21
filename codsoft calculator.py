# Task 1 @codsoft# python internship
"""designing a simple calculator"""

print("Welcome to the mini calculator made by Chirag Miglani")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option = int(input("Choose any operation (1/2/3/4): "))

if option in [1, 2, 3, 4]:
    digit1 = int(input("Enter the first number: "))
    digit2 = int(input("Enter the second number: "))

    if option == 1:
        final_result = digit1 + digit2
        operation = "Addition"
    elif option == 2:
        final_result = digit1 - digit2
        operation = "Subtraction"
    elif option == 3:
        final_result = digit1 * digit2
        operation = "Multiplication"
    elif option == 4:
        if digit2 != 0:
            final_result = digit1 / digit2
            operation = "Division"
        else:
            print("Error: Division by zero")
            final_result = None
            operation = "Division (oops showing error)"

    if final_result is not None:
        print(f"The result of {operation} is {final_result}")
    else:
        print(f"Cannot perform {operation} operation.")

    print("Thank you for using  my mini calculator!")
else:
    print("Invalid option selected. Please bro  choose a valid operation (1/2/3/4).")

