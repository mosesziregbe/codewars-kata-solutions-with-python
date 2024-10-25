# Unique In Order
# Implement the function unique_in_order which takes as argument a sequence and returns a
# list of items without any elements with the same value next to each other and
# preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3


def unique_in_order(sequence):
    results = []

    for element in sequence:
        # Only append if results is empty or element is different from last one
        if not results or element != results[-1]:
            results.append(element)

    return results





print(unique_in_order((1, 2, 2, 3, 3)))
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))



# Output

# [1, 2, 3]
# ['A', 'B', 'C', 'D', 'A', 'B']
# ['A', 'B', 'C', 'D', 'A', 'B']



# Notes:

# In Python, there are a few ways to check if a list is empty.

# Here are the common patterns:

results = []  # empty list

# Method 1: using 'not'
if not results:    # True if empty
    print("List is empty")

# Method 2: comparing length to 0
if len(results) == 0:    # True if empty
    print("List is empty")

# Method 3: comparing directly to empty list
if results == []:    # True if empty
    print("List is empty")

# The if not results is the most Pythonic and preferred way because:

# It's more concise
# It's more readable
# It works because empty sequences (lists, strings, etc.)
# are considered False in Python when converted to boolean

# Example:

# Empty sequences are "falsy"
empty_list = []
bool(empty_list)        # False
bool(not empty_list)    # True

# Non-empty sequences are "truthy"
non_empty = [1, 2, 3]
bool(non_empty)         # True
bool(not non_empty)