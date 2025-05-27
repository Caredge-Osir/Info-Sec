# Ask the user how many times they want to perform the calculation
num_trials = int(input("Enter the number of Trials: "))

# Loop for each trial
for trial in range(num_trials):
    # Get number of days from the user
    num_days = int(input("Enter the number of Days: "))
    
    # Calculate seconds in the given number of days
    seconds = num_days * 24 * 60 * 60
    
    # Display the result
    print(f"The number of Seconds in {num_days} Days is {seconds} Seconds")

print("End of Program")
