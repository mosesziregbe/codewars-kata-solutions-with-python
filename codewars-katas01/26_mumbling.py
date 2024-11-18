# Mumbling
# This time no story, no theory. The examples below show you how to
# write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(letters):
    return '-'.join((letter * index).title() for index, letter in enumerate(letters, 1))


print(accum("wwwy"))
print(accum("abcde"))
print(accum("cWat"))
print(accum("RqaEzty"))
print(accum("eerrQT"))


# Output:

# W-Ww-Www-Yyyy
# A-Bb-Ccc-Dddd-Eeeee
# C-Ww-Aaa-Tttt
# R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy
# E-Ee-Rrr-Rrrr-Qqqqq-Tttttt
