# Define the number of rows for the triangle
num_rows = 5
current_number = 1

# Outer loop for each row
for i in range(1, num_rows + 1):
    # Inner loop for each number in the row
    for j in range(1, i + 1):
        # Print the current number and a space
        print(current_number, end=" ")
        current_number += 1
    
    # Move to the next line for the next row
    print()