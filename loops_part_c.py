import random

# Generate a random number between 1 and 20
hidden = random.randint(1, 20)

# Print the random number generated (for testing purposes)
print(f"The hidden number is: {hidden}")

# Ask the user to enter a guess (number between 1 and 20)
while True:
    guess = int(input("Enter your guess (between 1 and 20): "))

    # Check if the guess is correct, too low, or too high
    if guess == hidden:
        print("Congratulations! Your guess is correct.")
        break  # Exit the loop if the guess is correct
    elif guess < hidden:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
