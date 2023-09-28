def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase.
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings match.
    return sorted(str1) == sorted(str2)
  
string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print("Are they anagrams?", result)