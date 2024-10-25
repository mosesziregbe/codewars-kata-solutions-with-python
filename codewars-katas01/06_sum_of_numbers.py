# Sum of Numbers
# Given two integers a and b, which can be positive or negative, find the sum of
# all the integers between and including them and return it.
# If the two numbers are equal return a or b.

# Note: a and b are not ordered!


def get_sum(a,b):
    my_sum = 0

    if a == b:
        my_sum += a

    else:
        for element in range(min(a, b), max(a, b) + 1):
            my_sum += element

    return my_sum

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)


# Your function should only return a number, not the explanation about how you get that number.


# one liner solution

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))



print(get_sum(-1, 0))
print(get_sum(-1, 2))
print(get_sum(0, 1))
print(get_sum(3, 4))
print(get_sum(5, 5))



# Output

# -1
# 2
# 1
# 7
# 5