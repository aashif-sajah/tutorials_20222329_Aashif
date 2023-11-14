def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

# Get user input for Celsius temperature


celsius_input = float(input("Enter temperature in Celsius: "))

# Call the function and print the result
result_fahrenheit = celsius_to_fahrenheit(celsius_input)
print("Temperature in Fahrenheit:", result_fahrenheit)
