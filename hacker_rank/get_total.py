

def getTotalX(a, b):
	print(a)
	print(b)
	i = 0
	a_len = len(a)
	b_len = len(b)

	while 1 < a_len:
		i += 1
		el = a[i]
		print(el)	
		if i == a_len:
			break


result = getTotalX([2, 3], [2, 4])
