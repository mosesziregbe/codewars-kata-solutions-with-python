# A Needle in the Haystack

# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full
# of junk but containing one "needle"

# After your function finds the needle it should return
# a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Example(Input --> Output)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# --> "found the needle at position 5"


def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'



print(find_needle(["hay", "needle", "junk"]))
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))



# Output:

# found the needle at position 1
# found the needle at position 5
