def make_sentence(word, part_of_speech):
    """
    Creates and prints a sentence using the word and part_of_speech.

    - part_of_speech 0 = noun
    - part_of_speech 1 = verb
    - part_of_speech 2 = adjective
    """
    if part_of_speech == 0:
        # If the part of speech is a noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # If the part of speech is a verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # If the part of speech is an adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # If the part of speech is invalid (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")  # Prompt user for input
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))  # Prompt for part of speech
    make_sentence(word, part_of_speech)  # Call the function to generate the sentence

# The following line ensures that the main function is called when the script is executed.
if __name__ == '__main__':
    main()
