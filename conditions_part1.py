while True:
    try:

        # Read in the person's age
        age = int(input("Enter your age: "))

        # Check if the person is old enough to vote
        if age >= 18:
            print("You can vote!")
            break
        else:
            print("You are not old enough to vote yet.")
            break
    except ValueError:
        print("Intiger required!!")
