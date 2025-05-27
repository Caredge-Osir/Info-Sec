# Define a function to compute the value based on the given logic
def compute_value():
    x = 0     # Initialize x to 0
    y = 20    # Start y at 20

    # Loop until y becomes less than 6
    while y >= 6:
        y -= 4           # Reduce y by 4 in each iteration
        x += 2 / y       # Add 2 divided by the new value of y to x

    return x             # Return the final result

# Call the function and print the result
print(compute_value())

# Indicate the end of the program
print("End of program")
