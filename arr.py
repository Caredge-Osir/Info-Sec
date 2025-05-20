arr=[]
for i in range(5):
    i=int(input("Enter the number: "))
    arr.append(i)       

print("The array is: ", arr)   
average=sum(arr)/len(arr)
print("The average is: ", average)
print("end of program")
# The code takes 5 numbers as input from the user, stores them in an array, and calculates the average of the numbers.