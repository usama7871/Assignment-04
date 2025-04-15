# Define the minimum voting age for each fictional country as constants
# Using ALL CAPS for constant variables is a good convention in Python
PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

# Define the main function where the actual logic will be written
def main():
    # Ask the user to input their age
    # The input function always returns a string, so we convert it to an integer using int()
    user_age = int(input("How old are you? "))

    # ------------------------------------------
    # Check if the user is old enough to vote in Peturksbouipo
    # If the user's age is greater than or equal to 16, they can vote
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")

    # ------------------------------------------
    # Check if the user is old enough to vote in Stanlau
    # If the user's age is 25 or more, they are eligible to vote here
    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")

    # ------------------------------------------
    # Check if the user is old enough to vote in Mayengua
    # Mayengua has a very high voting age (48), so check accordingly
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")

# ----------------------------------------------------
# This line runs the main() function only when this script is run directly
# It prevents the main function from running if this file is imported into another file
if __name__ == '__main__':
    main()
