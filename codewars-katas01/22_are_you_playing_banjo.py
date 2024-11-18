# Description:

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo"
# name + " does not play banjo"

# Names given are always valid strings.

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"



print(are_you_playing_banjo('tega'))
print(are_you_playing_banjo('ruth'))
print(are_you_playing_banjo('roseline'))
print(are_you_playing_banjo('dave'))
print(are_you_playing_banjo('zirkzee'))
print(are_you_playing_banjo('Roland'))


# Output:

# tega does not play banjo
# ruth plays banjo
# roseline plays banjo
# dave does not play banjo
# zirkzee does not play banjo
# Roland plays banjo


