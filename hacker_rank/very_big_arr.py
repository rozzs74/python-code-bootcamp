def aVeryBigSum(ar):
	ar_length = len(ar)
	i = 0
	total = 0000000000
	while ar_length > 0:
		el = ar[i]
		el_length = len(str(el))
		print(el_length)
		total = total + el
		i = i + 1	
		if i == ar_length:
			return total

result = aVeryBigSum([ 1000000001, 1000000002, 1000000003, 1000000004, 1000000005])

print(result)

