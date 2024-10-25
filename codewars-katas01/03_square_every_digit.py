# Square Every Digit

# In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out,
# because 9^2 is 81 and 1^2 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625
# because 7^2 is 49, 6^2 is 36, and 5^2 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!



def square_digits(num):
    results = ""
    for value in str(num):
        results += str(int(value) ** 2)

    return int(results)


print(square_digits(9119))
print(square_digits(765))
print(square_digits(8))



# one-liner solution

def square_digits(num):
    return int(''.join(str(int(x)**2) for x in str(num)))

print(square_digits(9119))
print(square_digits(765))
print(square_digits(8))



# Output

# 811181
# 493625
# 64