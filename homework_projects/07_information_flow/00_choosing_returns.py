ADULT_AGE = 18  # The legal age to be classified as an adult in the U.S.

def is_adult(age: int):
    # Check if the age is greater than or equal to the adult age
    if age >= ADULT_AGE:
        return True
    return False

def main():
    # Prompt the user to enter an age
    age = int(input("How old is this person?: "))
    # Output whether the person is an adult or not
    print(is_adult(age))

if __name__ == '__main__':
    main()
