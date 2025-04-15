def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:
        return True
    return False

def main():
    # Test the function with some sample values
    print(in_range(5, 1, 10))  # Expected output: True
    print(in_range(0, 1, 10))  # Expected output: False
    print(in_range(10, 1, 10)) # Expected output: True

if __name__ == '__main__':
    main()
