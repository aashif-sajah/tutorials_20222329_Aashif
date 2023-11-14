def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

# Ask the user for the conversion option
print("Choose an option:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

option = input("Enter your choice (1 or 2): ")

# Check the user's choice and perform the conversion
if option == '1':
    celsius_input = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(celsius_input)
    print("Converted temperature in Fahrenheit:", result)
elif option == '2':
    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(fahrenheit_input)
    print("Converted temperature in Celsius:", result)
else:
    print("Invalid option entered. Please enter '1' or '2'.")
