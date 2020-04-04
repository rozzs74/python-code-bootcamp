def plusMinus(array):
    array_length = len(array)
    i = 0
    counts = { 
        'positive': 0, 
        'negative':0 , 
        'zero': 0
    }
    quotient = None
    while array_length > 1:
        element = array[i]
        if element > 0:
            counts["positive"] = counts["positive"] + 1
        if element == 0:
            counts["zero"] = counts["zero"] + 1
        if element < 0:
            counts["negative"] = counts["negative"] + 1
        i = i + 1
        if i == array_length:
            break
    for item in counts.values():
        quotient = item / array_length
        print(f"{quotient:6f}")
    return
arr = plusMinus([-4,3,-9,0,4,1])
