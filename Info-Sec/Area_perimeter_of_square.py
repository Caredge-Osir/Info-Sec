def Area(side_length):
    """Returns the area of a Square."""
    return side_length ** 2

def Perimeter(side_length):
    """Returns the perimeter of a Square."""
    return 4 * side_length

no_of_squares = int(input("Enter the number of squares: "))

for n in range(no_of_squares):
    side_length = float(input(f"\nEnter the length of side {n + 1}: "))
    area = round(Area(side_length), 2)
    perimeter = round(Perimeter(side_length), 2)
    
    print(f"The area of the Square with side length {side_length} is {area}")
    print(f"The perimeter of the Square with side length {side_length} is {perimeter}")

print("\nEnd of program")
