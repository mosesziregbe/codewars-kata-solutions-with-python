# Sum of two lowest positive integers

# Create a function that returns the sum of the two lowest
# positive numbers given an array of minimum 4 positive integers.
# No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77],
# the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.



# using list slicing

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([9, 8, 2, 3, 5]))
print(sum_two_smallest_numbers(([19, 5, 42, 2, 77])))
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))



# Output:
#
# 5
# 7
# 3453455