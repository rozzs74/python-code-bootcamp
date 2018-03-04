# ANIMAL CRACKERS: 
# Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(word):
    split_word = word.split()
    return split_word[0][0].lower() == split_word[1][0].lower()

print(animal_crackers("John Royce")) # False