# find biggest digit out of three
a=int(input("Enter the number\n"))

# Convert the number to a string
num_str = str(a)

# Initialize the maximum digit with the first digit
max_digit = int(num_str[0])

# Iterate through the remaining digits
for digit_char in num_str[1:]:
    digit = int(digit_char)
    if digit > max_digit:
        max_digit = digit

# Print the result
print(f"The largest digit in {a} is {max_digit}")
