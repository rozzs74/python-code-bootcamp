def reverse_words_order_and_swap_cases(sentence):
    a = " ".join(sentence.split()[::-1]) 
    return a.swapcase()
a = reverse_words_order_and_swap_cases("aWESOME is cODING")
print(a)
