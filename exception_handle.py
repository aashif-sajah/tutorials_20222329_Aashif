while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
        print("Result:", result)
        break  # Break out of the loop if successful
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero denominator.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
