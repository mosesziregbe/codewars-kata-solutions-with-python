# Stop gninnipS My sdroW!

# Write a function that takes in a string of one or more words,
# and returns the same string, but with all words that have five
# or more letters reversed (Just like the name of this Kata).

# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

# Examples:
#
# "Hey fellow warriors"  --> "Hey wollef sroirraw"
# "This is a test        --> "This is a test"
# "This is another test" --> "This is rehtona test"


def spin_words(text):
    # Split into words
    words = text.split()

    # Process each word, find the number of words
    # then iterate through the range(number of words)
    for i in range(len(words)):
        # If word is 5 or more letters, reverse it
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]  # assign reversed word to that index position

    # Join back with spaces
    return ' '.join(words)



print(spin_words("okay let me check this"))
print(spin_words("okay chamomile tea is great"))
print(spin_words("Hey fellow warriors"))
print(spin_words("tega"))



# Output

# okay let me kcehc this
# okay elimomahc tea is taerg
# Hey wollef sroirraw
# tega