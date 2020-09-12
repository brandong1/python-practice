# **kwargs - gathers remaining keyword arguments as a dictionary

def fav_colors(**kwargs):
    for person, color in kwargs.items():
    # use .items() because I want the key and value from the dictionary
        print(f"{person}'s favorite color is {color}")

fav_colors(brandon="purple", ronda="green", judy="red")

####################
# I check if kwargs contains "prefix".
# If it does, I return the value of prefix + the word
# Otherwise, I check to see if "suffix" was provided as a kwarg
# If it was, I return the word followed by the value of suffix
# Otherwise, I just return the word on its own.

# Define combine_words below:
def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word
