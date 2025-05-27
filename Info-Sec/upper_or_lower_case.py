def upper_case(s):
    """Returns True if s is all uppercase, False if all lowercase, None if mixed."""
    if s.isupper():
        return True
    elif s.islower():
        return False
    else:
        return None

def lower_case(s):
    """Returns True if s is all lowercase, False if all uppercase, None if mixed."""
    if s.islower():
        return True
    elif s.isupper():
        return False
    else:
        return None

# Get number of character inputs to process
no_of_characters = int(input("Enter the number of characters on trial: "))

# Loop through each input
for n in range(no_of_characters):
    s = input("Enter the character: ")
    
    # Check and report casing
    if upper_case(s) == True:
        print("The character is in uppercase")
    elif lower_case(s) == True:
        print("The character is in lowercase")

print("End of program")
