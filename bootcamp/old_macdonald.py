#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# My solution
# def old_macdonald(word):
#     if(len(word) <= 3):
#         print("Please enter four letter word")
#         return False
#     else:
#         first_letter = word[0].upper()
#         fourth_letter = word[3].upper()
#         sliced_letter = word[1:3]
#         remaining_letter = word[4:]
#         return f"{first_letter}{sliced_letter}{fourth_letter}{remaining_letter}"


# Portilla

def old_macdonald(word):
    if len(word) > 3:
        return f"{word[:3].capitalize()}{word[3:].capitalize()}"
    else:
        return 'Name is too short!'

# print(old_macdonald("macdonald"))   # MacDonald
print(old_macdonald("royce"))