# Ask the user 'Do you like Python? (yes/no): '
user_response = input('Do you like Python? (yes/no): ')

# Check user response using if-elif-else structure
if user_response.lower() == 'yes':
    print("You are on the right course!")
elif user_response.lower() == 'no':
    print("You might change your mind.")
else:
    print("I did not understand.")
