def most_frequent_character(input_string):
    # Create a dictionary to store character frequencies.
    char_count = {}

    # Iterate through the string to count character frequencies.
    for char in input_string:
        if char.isalpha():  # You can exclude non-alphabetic characters if desired.
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Find the character with the maximum frequency.
    most_frequent_char = max(char_count, key=char_count.get)

    return most_frequent_char

input_string = "hello, world!"
result = most_frequent_character(input_string)
print("Most frequent character:", result)