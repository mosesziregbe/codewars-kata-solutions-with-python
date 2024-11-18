
# Sum without highest and lowest number

# Sum all the numbers of a given array ( cq. list ), except the
# highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element
# at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6

# Input validation
# If an empty value ( null, None, Nothing, nil etc. ) is given
# instead of an array, or the given array is an empty list or
# a list with only 1 element, return 0.



def sum_array(arr):
	return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


print(sum_array([-652, -698, 11, 5]))
print(sum_array([42, -78, -583, -562, 301]))
print(sum_array([-561, 42, -1, 6, 98, -570, 5]))
print(sum_array([846, -66, 362, -246, -542]))
print(sum_array([3]))
print(sum_array(None))


# Output

# -647
# -598
# -509
# 50
# 0
# 0

