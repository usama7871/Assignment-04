def main():
    # Prompt user to enter a fruit
    fruit = input("Enter a fruit: ")

    # Call the num_in_stock function to check the stock
    stock = num_in_stock(fruit)

    # Check if stock is greater than 0 or not
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    If the fruit is not in stock, it returns 0.
    """
    # Check for different fruits and return their stock count
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # If the fruit is not in stock
        return 0

# This ensures the main function is executed when the script runs
if __name__ == '__main__':
    main()
