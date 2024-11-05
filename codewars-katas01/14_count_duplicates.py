# Counting Duplicates
# Count the number of Duplicates


# Write a function that will return the count of distinct
# case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string.

# The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.


def duplicate_count(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return sum(1 for count in char_counts.values() if count > 1)


# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice



# Explanation:


def duplicate_count(text):

    # 1. Convert text to lowercase so 'A' and 'a' count as same character

    text = text.lower()

    # Example: "aAbBcde" becomes "aabbcde"

    # 2. Create empty dictionary to store character counts

    char_counts = {}

    # 3. Count each character

    for char in text:
        if char in char_counts:  # If we've seen this character before
            char_counts[char] += 1  # Add 1 to its count

        else:  # If this is the first time seeing this character
            char_counts[char] = 1  # Start its count at 1

    # Let's see what happens with "aabbcde":
    # First loop:  char = 'a' → char_counts = {'a': 1}
    # Second loop: char = 'a' → char_counts = {'a': 2}
    # Third loop:  char = 'b' → char_counts = {'a': 2, 'b': 1}
    # Fourth loop: char = 'b' → char_counts = {'a': 2, 'b': 2}
    # Fifth loop:  char = 'c' → char_counts = {'a': 2, 'b': 2, 'c': 1}
    # Sixth loop:  char = 'd' → char_counts = {'a': 2, 'b': 2, 'c': 1, 'd': 1}
    # Seventh loop: char = 'e' → char_counts = {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1}

    # 4. Count how many characters appear more than once

    return sum(1 for count in char_counts.values() if count > 1)

    # char_counts.values() gives us [2, 2, 1, 1, 1]
    # count > 1 checks each value: [True, True, False, False, False]
    # sum(1 for...) counts how many Trues: 2


print(duplicate_count("aabbcde"))  # 2 (because 'a' and 'b' appear twice)
print(duplicate_count("abcde"))    # 0 (no duplicates)
print(duplicate_count("aabBcde"))  # 2 (because 'a' and 'b' appear twice, case-insensitive)
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
print(duplicate_count("aaaAAA111"))
print(duplicate_count("indivisibility"))
print(duplicate_count("mosesTEGAziregbe"))
print(duplicate_count("abcde"))



# Output

# 2
# 0
# 2
# 2
# 2
# 2
# 1
# 3
# 0
