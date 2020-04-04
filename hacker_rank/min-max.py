def miniMaxSum(array):
	array_length = len(array)	
	min_element = min(array)
	max_element = max(array)
	i = 0
	min_total = 0
	max_total = 0
	all_equal = False
	while array_length > 1:
		item = array[i]
		if item >= min_element and item < max_element:
			min_total  = min_total + item
		if item <= max_element and item != min_element:	
			max_total = max_total + item
		if item == min_element and item == max_element:
			max_total = max_total + item
			min_total = min_total + item
			all_equal = True
		i = i + 1
		if i == array_length:
			if all_equal == True:
				print(f"{min_total - min_element} {max_total - max_element}")	
			else :
				print(f"{min_total} {max_total}")
			break
	return 1
a = miniMaxSum([1,2,3,4,5])
a = miniMaxSum([4,-1,3,6,9])
a = miniMaxSum([4,1,3,6,9])

a = miniMaxSum([5,5,5,5,5])