



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
	a_length = len(a)
    b_length = len(b)
    i = 0
    score = [0, 0]
    while a_length == b_length:
        a_element = a[i]
        b_element = b[i]
        if a_element > b_element:
            score[0] = score[0] + 1
        elif a_element < b_element:
        	score[1] = score[1] + 1
        i = i + 1
        if i == a_length & i == b_length:
			return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
	print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
