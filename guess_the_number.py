from random import randint
computer_choice = randint(1, 100)
while True:
    user_input = input("Enter a number between 1 and 100: ")
    if not user_input.isdigit():
        print("Invalid input. Try again!")
        continue
    user_number = int(user_input)
    if user_number < 1 or user_number > 100:
        print("The range is [1, 100]. Try again! ")
    elif user_number < computer_choice:
        print("Too low!")
    elif user_number > computer_choice:
        print("Too high!")
    else:
        print("You guess it!")
        break

