# single_letter_count function takes two parameters (two strings). First param is a word, second is a letter.
# Function returns the number of times the letter appears in the word; case insensitive
# If letter is not found in the word, return 0

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())