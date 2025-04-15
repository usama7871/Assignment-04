MAX_TERM_VALUE = 10000  # The maximum value for the Fibonacci sequence

def main():
    curr_term = 0  # The 0th Fibonacci number
    next_term = 1  # The 1st Fibonacci number

    # Print Fibonacci terms as long as the current term is less than or equal to MAX_TERM_VALUE
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)  # Print the current Fibonacci term
        # Update the terms for the next iteration
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next


# The provided line is required to call the main() function
if __name__ == '__main__':
    main()
