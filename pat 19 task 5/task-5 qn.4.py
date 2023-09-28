def count_unique_characters(input_string):
    # Initialize an empty set to store unique characters
    unique_chars = set()
    
    # Iterate through each character in the input string
    for char in input_string:
        # Add the character to the set
        unique_chars.add(char)
    
    # Return the number of unique characters in the set
    return len(unique_chars)

input_string= input()
count = count_unique_characters(input_string)
print("Number of unique characters:", count)