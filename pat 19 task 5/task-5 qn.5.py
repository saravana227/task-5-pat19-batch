def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for case-insensitive comparison
    input_string = input_string.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return input_string == input_string[::-1]

input_string = input()
result = is_palindrome(input_string)
print(result)