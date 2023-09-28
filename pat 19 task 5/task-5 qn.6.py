def longest_common_substring(str1, str2):
    # Initialize a 2D table to store the length of common substrings.
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to keep track of the length and end position of the longest common substring.
    max_length = 0
    end_position = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i
            else:
                dp[i][j] = 0

    # Extract the longest common substring using the end position.
    longest_common_substring = str1[end_position - max_length:end_position]

    return longest_common_substring

str1 = "abcdefg"
str2 = "xyzabcde"
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)