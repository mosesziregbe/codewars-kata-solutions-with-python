# Categorize New Member

# The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
# They would like your help with an application form that will tell prospective
# members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap
# greater than 7. In this croquet club, handicaps range from -2 to +26; the
# better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. Each pair contains information for a
# single potential member. Information consists of an integer for the person's age
# and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open or Senior)
# stating whether the respective member is to be placed in the senior or open category.

# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]


def open_or_senior(data):
    membership_category = []

    for pair in data:
        if pair[0] >= 55 and pair[1] > 7:
            membership_catgeory.append('Senior')
        else:
            membership_category.append('Open')

    return membership_category


# using list comprehension

def open_or_senior(data):
    return ['Senior' if pair[0] >= 55 and pair[1] > 7 else 'Open' for pair in data]



print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
print(open_or_senior([[55, 20], [61, 9], [61, 12], [47, 6], [21, 21], [78, 9]]))


# Output

# ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']
# ['Senior', 'Senior', 'Senior', 'Open', 'Open', 'Senior']


# Notes:

# The general structure for including an if-else statement in
# a list comprehension is:

# new_list = [result_if_true if condition else result_if_false for item in iterable]

# Example Explanation
# For instance, if you want to create a list that classifies numbers as
# "Even" or "Odd", you could write:

# even_odd_list = ['Even' if x % 2 == 0 else 'Odd' for x in my_list]


