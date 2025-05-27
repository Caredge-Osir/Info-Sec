import math  # Import the math module to access math.pi

# Get the number of spheres to calculate
no_of_spheres = int(input("Enter the number of Spheres: "))

# Loop through each sphere
for n in range(no_of_spheres):
    radius = float(input("Enter the radius of the Sphere: "))
    
    # Calculate volume: (4/3) * π * r³
    volume = (4/3) * math.pi * (radius ** 3)
    
    # Print the volume rounded to 2 decimal places
    print(f"The volume of the Sphere with Radius {radius} is {round(volume, 2)}")

print("End of Program")
