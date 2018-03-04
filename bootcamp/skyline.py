# Define a func called my func that takes string return string where every even letter is uppercase
# and every odd letter is lowercase 


def skyline(word):
    word_list = []
    for index in range(0, len(word)):
        if index % 2 == 0:
            even_letters = word[index].upper()
            word_list.append(even_letters)
        else:     
            odd_letters = word[index].lower()
            word_list.append(odd_letters)
        
    return ''.join(word_list)
        
    
print(skyline("John Royce"))