def main():
    # Dictionary of fruits and their individual prices in dollars
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0.0  # Variable to accumulate total cost

    # Loop over each fruit and ask user how many they want
    for fruit_name in fruits:
        try:
            quantity = int(input(f"How many ({fruit_name}) do you want?: "))
            if quantity < 0:
                print("Quantity can't be negative. Assuming 0.")
                quantity = 0
        except ValueError:
            print("Invalid input. Assuming 0.")
            quantity = 0

        # Update total cost
        total_cost += quantity * fruits[fruit_name]

    # Final output
    print(f"Your total is ${total_cost:.2f}")


# Required Python boilerplate
if __name__ == '__main__':
    main()
