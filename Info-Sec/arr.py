# Initialize an empty list to store user input
arr = []

# Loop 5 times to get 5 numbers from the user
for i in range(5):
    i = int(input("Enter the number: "))  # Take input, convert to int
    arr.append(i)  # Add the number to the list

# Print the list of numbers entered by the user
print("The Array is: ", arr)

# Calculate the average by dividing the sum of the list by its length
average = sum(arr) / len(arr)

# Print the average of the numbers
print("The Average is: ", average)

# Indicate the end of the program
print("end of program")
