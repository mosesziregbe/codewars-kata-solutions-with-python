# Sort the odd

# Task
# You will be given an array of numbers. You have to sort the odd numbers
# in ascending order while leaving the even numbers at their original positions.

# Example
# [7, 1, 2, 3, 5] -> [1, 3, 2, 5, 7]

def sort_array(source_array):
    # Get odd numbers and sort them
    odds = sorted([x for x in source_array if x % 2 != 0])

    # Counter to track position in odds list
    odds_index = 0

    # Result list
    result = []

    # Go through original array
    for num in source_array:
        # If number is even, keep it
        if num % 2 == 0:
            result.append(num)
        # If odd, take next number from sorted odds
        else:
            result.append(odds[odds_index])
            # odds_index = odds_index + 1
            odds_index += 1

    return result


# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]



print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(sort_array([7, 1, 2, 3, 5]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([7, 1]))


# output:

# [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
# [1, 3, 2, 5, 7]
# [3, 8, 6, 5, 4]
# [1, 7]