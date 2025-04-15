def average(a: float, b: float):
    """
    Returns the number which is half way between a and b
    """
    sum = a + b  # Sum of the two numbers
    return sum / 2  # Divide the sum by 2 to find the average

def main():
    # Call the average function with two sets of numbers
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    # Now average the results of the two averages
    final = average(avg_1, avg_2)
    
    # Print out all the averages
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

# This is the required boilerplate to ensure the main() runs
if __name__ == '__main__':
    main()
