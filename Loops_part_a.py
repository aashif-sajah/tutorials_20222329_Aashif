# Initialize variable 'hidden' with a value of 6
hidden = 6

# Ask the user to enter a guess (number between 1 and 20)
while True:
    guess = int(input("Enter your guess (between 1 and 20): "))

    # Check if the guess is correct
    if guess == hidden:
        print("Congratulations! Your guess is correct.")
        break  # Exit the loop if the guess is correct
    else:
        print("Incorrect guess. Try again.")
