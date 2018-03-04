# Description: Program that can determine the lower and upper case of a word / sentence string
# Author: John Royce Punay
# Date created: March 4, 2018 8:47 AM

from unicodedata import numeric

WORD_LISTS = []
UPPER_CASE = 0
LOWER_CASE = 0


# Solution 2 Check if word string consits of number
def is_number(word):
    try:
        float(word)
        return True
    except ValueError:
        pass
    try:
        numeric(word)
        return True
    except (TypeError, ValueError):
        pass
    return False

def process_words(words): 
    global UPPER_CASE, LOWER_CASE
    for letter in words.replace(" ",""):
        if letter.isupper():
            UPPER_CASE += 1
        else:
            LOWER_CASE += 1
    return dict({"UPPER_CASE": UPPER_CASE, "LOWER_CASE": LOWER_CASE, "WORDS": words})


# Solution 1 
def is_alphabet(words):
    result = None
    global WORD_LISTS
    
    for character in words.replace(" ", "") :
        WORD_LISTS.append(character)
        if character.isalpha():
            result = True
        else:
            result = False
    return result

def transform_word():
    global WORD_LISTS, UPPER_CASE, LOWER_CASE

    for index in range(0, len(WORD_LISTS)): 
        if WORD_LISTS[index].isupper():
            UPPER_CASE  += 1
        else:
            LOWER_CASE += 1
            
    formatted_word = "".join(WORD_LISTS)
    return dict({"UPPER_CASE": UPPER_CASE, "LOWER_CASE": LOWER_CASE, "WORDS": formatted_word})

def main():
    print("<----- Upper and lower case checker in your word ---->")
    global WORD_LISTS
    while True:
        user_input = input("Please enter your desired word: ")
        is_input_valid = is_alphabet(user_input)

        if is_input_valid:
            result = transform_word()
            print(f"Original string {result['WORDS']}")
            print(f"No. of Upper case characters {result['UPPER_CASE']}")
            print(f"No. of Lower case characters {result['LOWER_CASE']}")
            break
        else:
            print("Please enter valid word like without number: ")
            WORD_LISTS = []
            continue

main()


