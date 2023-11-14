import random

# Generate a random number between 1 and 20
hidden_number = random.randint(1, 20)

# Allow the user a maximum of five attempts to guess the number
for _ in range(5):
    try:
        # Get user input for the guess
        user_guess = int(input("Enter your guess (between 1 and 20): "))

        # Check if the guess is correct, too low, or too high
        if user_guess == hidden_number:
            print(f"Congratulations! Your guess is correct. It took you {_ + 1} attempts.")
            break  # Exit the loop if the guess is correct
        elif user_guess < hidden_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

# Display appropriate message based on the outcome
if user_guess != hidden_number:
    print(f"Sorry, you did not guess the number. The hidden number was {hidden_number}.")
