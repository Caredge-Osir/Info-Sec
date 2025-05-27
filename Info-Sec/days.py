# Ask the user how many times they want to perform the calculation
num_trials = int(input("Enter the number of trials: "))

# Loop for each trial
for trial in range(num_trials):
    # Get number of days from the user
    num_days = int(input("Enter the number of days: "))
    
    # Calculate seconds in the given number of days
    seconds = num_days * 24 * 60 * 60
    
    # Display the result
    print(f"The number of seconds in {num_days} days is {seconds} seconds")

print("End of program")
