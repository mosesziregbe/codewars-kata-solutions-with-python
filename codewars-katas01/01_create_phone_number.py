# Create Phone numbers

# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"


def create_phone_number(numbers):
    nums = ''.join(map(str, numbers))

    return f"({nums[:3]}) {nums[3:6]}-{nums[6:]}"




# Explanation

# first, we use the map function to convert the numbers into
# strings, however this gives us an iterator object

# join() can work with any iterable that contains string elements,
# including iterator objects from map(). When join() processes an iterator,
# it consumes the iterator elements one by one

# The key point is that join() doesn't need a string or list specifically -
# it just needs any iterable that yields strings, which map(str, numbers) provides.

# finally use a formatted string literal to return the phone number, while
# doing the logic of slicing inside it


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(create_phone_number(numbers))



# Output

# (123) 456-7890