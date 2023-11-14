def calculator(integer1, operator, integer2):
    try:
        if operator == '+':
            result = integer1 + integer2
        elif operator == '-':
            result = integer1 - integer2
        elif operator == '*':
            result = integer1 * integer2
        elif operator == '/':
            result = integer1 / integer2
        else:
            raise ValueError("Invalid operator")

        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError as e:
        return f"Error: {e}"


# Get user input for the calculation
try:
    integer1 = int(input("Enter the first integer: "))
    operator = input("Enter the operator (+, -, *, /): ")
    integer2 = int(input("Enter the second integer: "))

    result = calculator(integer1, operator, integer2)
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
