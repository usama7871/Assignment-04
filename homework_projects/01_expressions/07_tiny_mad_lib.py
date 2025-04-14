"""
Mad Libs Word Game
------------------
This program creates a fun sentence by prompting the user for
an adjective, noun, and verb, then inserting them into a template.

The program demonstrates:
- String constants
- User input handling
- String concatenation
- Basic text formatting
"""

# Constant containing the beginning of our Mad Libs sentence
# The user's words will complete this sentence
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my "

def main():
    """
    Main function that:
    1. Gets an adjective, noun, and verb from the user
    2. Combines them with the sentence starter
    3. Prints the completed Mad Libs sentence
    """
    
    # Get adjective from user
    # input() pauses execution and waits for user to type something
    # The prompt tells the user what kind of word we want
    adjective = input("Please type an adjective and press enter. ")
    
    # Get noun from user
    # Each input is stored in a separate variable with a descriptive name
    noun = input("Please type a noun and press enter. ")
    
    # Get verb from user
    verb = input("Please type a verb and press enter. ")
    
    # Combine all parts to form the complete sentence
    # Using f-string for clean string formatting (Python 3.6+)
    # The \ at the end of the line continues the statement to the next line
    print(f"{SENTENCE_START}{adjective} {noun} {verb}!")
    
    # Alternative version using concatenation:
    # print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Standard Python idiom to check if running directly
if __name__ == '__main__':
    # Execute the main program
    main()