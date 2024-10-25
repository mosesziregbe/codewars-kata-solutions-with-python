# Write Number in Expanded Form

# You will be given a number and you will need to return it as
# a string in Expanded Form.

# For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"


def expanded_form(num):
    # Convert number to string to process each digit
    num_str = str(num)
    result = []

    # Process each digit
    for i, digit in enumerate(num_str):
        if digit != '0':  # Only process non-zero digits
            # Calculate place value (for 347, first 7 has 10^0, 4 has 10^1, 3 has 10^2)
            place_value = len(num_str) - i - 1
            # Add the expanded number (digit * 10^place_value)
            result.append(digit + '0' * place_value)

    # Join with ' + '
    return ' + '.join(result)


print(expanded_form(347))
print(expanded_form(299885))
print(expanded_form(70304))
print(expanded_form(12))


# Output

# 300 + 40 + 7
# 200000 + 90000 + 9000 + 800 + 80 + 5
# 70000 + 300 + 4
# 10 + 2