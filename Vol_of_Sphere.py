No_of_spheres = int(input("Enter the number of spheres: "))
for n in range(No_of_spheres):
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4/3) * 3.142 * (radius ** 3)
    print("The volume of the sphere with radius", radius, "is", volume)
    
print("End of program")