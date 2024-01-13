def word_count(sentence):
    # Split the sentence into words using whitespace as a delimiter
    words = sentence.split()
    
    # Return the count of words in the sentence
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")

    # Check for empty input
    if not user_input.strip():
        print("Error: Please enter a valid sentence or paragraph.")
        return

    # Call the word_count function to get the count of words
    count = word_count(user_input)

    # Display the word count to the console
    print(f"Word count: {count}")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()
