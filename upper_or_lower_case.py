def upper_case(s):
    """
    This function takes a string and returns True if the string is in uppercase,
    False if it is in lowercase, and None if it contains both uppercase and lowercase letters.
    """
    if s.isupper():
        return True
    elif s.islower():
        return False
    else:
        return None
    
def lower_case(s):
    """
    This function takes a string and returns True if the string is in lowercase,
    False if it is in uppercase, and None if it contains both uppercase and lowercase letters.
    """
    if s.islower():
        return True
    elif s.isupper():
        return False
    else:
        return None
    
no_of_characters = int(input("Enter the number of characters on trial: "))
for n in range(no_of_characters):
    s = input("Enter the character: ")
    if upper_case(s) == True:
        print("The character is in uppercase")
    elif lower_case(s) == True:
        print("The character is in lowercase")
    
print("End of program")
# The code defines two functions, upper_case and lower_case, to check if a string is in uppercase or lowercase.