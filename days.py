trials= input("Enter the number of trials: ")
for n in range(int(trials)):
    no_of_days=input("Enter the number of days: ")
    y=int(no_of_days) * 24 * 60 * 60
    print("The number of seconds in", no_of_days, "days is", y,"seconds")
print("End of program")   