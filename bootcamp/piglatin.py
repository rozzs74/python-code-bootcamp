#PIG LATIN GAME
# If word starts with a vowel add 'ay' to end
# If word does not start with a vowel, put the first letter at the end, then add 'ay'
# example word --> ordway
# example apple --> appleay


def pig_latin(word):

    first_letter = word[0]

    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin('word'))

    