def upper_case(s):
    """Returns True if s is all Uppercase, False if all lowercase, None if Mixed."""
    if s.isupper():
        return True
    elif s.islower():
        return False
    else:
        return None

def lower_case(s):
    """Returns True if s is all Lowercase, False if all uppercase, None if Mixed."""
    if s.islower():
        return True
    elif s.isupper():
        return False
    else:
        return None

# Get number of character inputs to process
no_of_characters = int(input("Enter the number of characters on Trial: "))

# Loop through each input
for n in range(no_of_characters):
    s = input("Enter the Character: ")
    
    # Check and report casing
    if upper_case(s) == True:
        print("The character is in Uppercase")
    elif lower_case(s) == True:
        print("The character is in Lowercase")

print("End of Program")
