import statistics
from typing import List
import sys

def get_valid_number(prompt: str) -> int:
    """Get a valid number from user input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_statistics(numbers: List[int]) -> dict:
    """Calculate various statistics for the given list of numbers."""
    if not numbers:
        return {}
    
    return {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "mode": statistics.mode(numbers) if len(numbers) > 1 else numbers[0],
        "standard_deviation": statistics.stdev(numbers) if len(numbers) > 1 else 0,
        "variance": statistics.variance(numbers) if len(numbers) > 1 else 0,
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers)
    }

def main():
    # Initialize an empty list to store user input
    numbers = []
    
    # Get the number of elements from user
    try:
        n = get_valid_number("How many numbers would you like to enter? ")
        if n <= 0:
            print("Please enter a positive number!")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(0)

    # Collect numbers from user
    print(f"\nEnter {n} numbers:")
    for i in range(n):
        num = get_valid_number(f"Enter number {i+1}: ")
        numbers.append(num)

    # Sort the numbers
    numbers.sort()
    
    # Print the sorted list
    print("\nSorted Array:", numbers)
    
    # Calculate and display statistics
    stats = calculate_statistics(numbers)
    
    print("\nStatistical Analysis:")
    print("-" * 20)
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Median: {stats['median']:.2f}")
    print(f"Mode: {stats['mode']}")
    print(f"Standard Deviation: {stats['standard_deviation']:.2f}")
    print(f"Variance: {stats['variance']:.2f}")
    print(f"Minimum: {stats['min']}")
    print(f"Maximum: {stats['max']}")
    print(f"Sum: {stats['sum']}")
    
    # Additional analysis
    print("\nAdditional Analysis:")
    print("-" * 20)
    print(f"Range: {stats['max'] - stats['min']}")
    print(f"Count: {len(numbers)}")
    
    # Check if numbers are evenly distributed
    if len(numbers) > 1:
        if abs(stats['mean'] - stats['median']) < 0.1:
            print("The numbers appear to be evenly distributed")
        else:
            print("The numbers appear to be skewed")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    finally:
        print("\nProgram execution completed.")