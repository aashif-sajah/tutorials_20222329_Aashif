def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

# Get user input for dimensions
length = float(input("Enter the length of the box: "))
width = float(input("Enter the width of the box: "))
height = float(input("Enter the height of the box: "))

# Call the function and print the result
box_volume = calculate_volume(length, width, height)
print("Volume of the box:", box_volume)
