def Area(side_length):
    """
    Calculate the area of a square given the length of its side.
    
    Parameters:
    side_length (float): The length of the side of the square.
    
    Returns:
    float: The area of the square.
    """
    return side_length ** 2
def Perimeter(side_length):
    """
    Calculate the perimeter of a square given the length of its side.
    
    Parameters:
    side_length (float): The length of the side of the square.
    
    Returns:
    float: The perimeter of the square.
    """
    return 4 * side_length


no_of_squares = int(input("Enter the number of squares: "))
for n in range(no_of_squares):
    side_length = float(input("Enter the length of the side of the square: "))
    Area_of_square = Area(side_length)
    print("The area of the square with side length", side_length, "is", Area_of_square)
    Perimeter_of_square = Perimeter(side_length)
    print("The perimeter of the square with side length", side_length, "is", Perimeter_of_square)
print("End of program")