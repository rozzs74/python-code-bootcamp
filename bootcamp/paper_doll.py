# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

# My solution
# def paper_doll(word):
#     tripled_letter_list = []

#     for letter in word:
#         tripled_letter = letter * 3
#         tripled_letter_list.append(tripled_letter)
    
#     return "".join(tripled_letter_list)

# Portilla sol
def paper_doll(text):
    result = ''
    for char in text:
        result += char *3
    
    return result


print(paper_doll("Hello"))