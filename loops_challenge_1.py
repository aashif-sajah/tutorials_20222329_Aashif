while True:
    try:
        # Display menu options
        print("Menu Options:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Quit")

        # Get user input for menu option
        user_choice = int(input("Enter your choice (1-4): "))

        # Process the user's choice
        if user_choice == 1:
            print("1 selected")
        elif user_choice == 2:
            print("2 selected")
        elif user_choice == 3:
            print("3 selected")
        elif user_choice == 4:
            print("Quit selected")
            break  # Exit the loop if the user chooses to quit
        else:
            print("Option not recognized")

    except ValueError:
        print("Invalid input. Please enter a number.")
