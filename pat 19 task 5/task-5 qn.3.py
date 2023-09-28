def remove_vowels(input_string):
    # Initialize an empty string to store the result
    result = ""
    
    # Define a set of vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Iterate through each character in the input string
    for char in input_string:
        # If the character is not in the set of vowels, add it to the result string
        if char not in vowels:
            result += char
    
    return result

input_string=input()
result = remove_vowels(input_string)
print(result)