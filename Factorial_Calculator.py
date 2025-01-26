print("Marlowe's Factorial Calculator")

#defines function to calculate the factorial of user input
def calculate_factorial(number):
    counter = number - 1
    factorial = number
    while counter > 0:
        factorial *= counter
        counter -= 1
    print(f"The factorial of {number} is {factorial}.")

#begins while loop to repeatedly request integer from user or quit
#rejects non-integer values that aren't q
#converts to int and rejects numbers greater than 1000
#calls function if conditions met
while True:
    user_input = input("Enter an integer between 1-1000 to find its factorial or type q to quit: "
    )
    if user_input == "q":
        print("Thanks for using Marlowe's factorial calculator! See you later!")
        break
    else:
        if not user_input.isnumeric():
            print("Please enter an integer or q to quit: ")
        else:
            number = int(user_input)
            if number > 1000:
                print("Factorials can get very large very quickly, please limit input to 1-1000 to avoid overloading memory.")
            else:
                calculate_factorial(number)

