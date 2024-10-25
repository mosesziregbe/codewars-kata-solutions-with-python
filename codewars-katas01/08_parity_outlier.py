# Find The Parity Outlier

# You are given an array (which will have a length of at least 3,
# but could be very large) containing integers.

# The array is either entirely comprised of odd integers or
# entirely comprised of even integers except for a single integer N.

# Write a method that takes the array as an argument
# and returns this "outlier" N.


def find_outlier(integers):

    # Check if we're looking for an odd or even number
    # by checking first 3 numbers

    evens = 0
    odds = 0

    # Count evens and odds in first 3 numbers
    for i in integers[:3]:
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    # If majority are even, we're looking for the odd number
    if evens > odds:
        # Find the odd number
        for num in integers:
            if num % 2 != 0:  # stops when the odd number is found
                return num
    else:
        # Find the even number
        for num in integers:
            if num % 2 == 0:  # stops when the even number is found
                return num



# Notes:

# First solution is more efficient for large lists
# Second solution is more elegant but less performant

# In real-world applications with large datasets, the
# first solution might be better


def find_outlier(integers):
    # Create two lists: one of evens, one of odds
    evens = [num for num in integers if num % 2 == 0]
    odds = [num for num in integers if num % 2 != 0]

    # Return the only number in whichever list has length 1
    return evens[0] if len(evens) == 1 else odds[0]


# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))


# Output

# 160
# 11