# Your goal in this kata is to implement a difference function, which subtracts
# one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]



def array_diff(a, b):

    results = []

    for element in a:
        if element not in set(b):
            results.append(element)

    return results

print(array_diff([1,2,2,2,3],[2]))
print(array_diff([1,2],[1]))



# Output

# [1, 3]
# [2]




# list comprehension

def array_diff(a, b):
    return [element for element in a if element not in set(b)]

print(array_diff([1,2,2,2,3],[2]))
print(array_diff([1,2],[1]))


# Output

# [1, 3]
# [2]