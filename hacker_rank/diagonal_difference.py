
def diagonalDifference1(arr):
	column = len(arr)
	print(f"Column {column} x {column}")
	first_stepper = 0
	print(f"first_stepper {first_stepper}")
	second_stepper = column - 1
	fd = 0 
	sd = 0
	for  i in arr:
		fd = fd + i[first_stepper];
		first_stepper = first_stepper + 1
		sd = sd + i[second_stepper]
		second_stepper = second_stepper - 1
	return abs(fd-sd)
# a = diagonalDifference1([[-1,1,-7,-8], [-10,-8,-5,-2], [0,9,7,-1], [4,4,-2,1]])

# def diagonalDifference2(items):
# 	items_length = len(items)
	
# 	print(f"items_length {items_length	}")
# 	# first_stepper = (items_length - 1) // 2
# 	# print(f"first_stepper {first_stepper}")
# 	# second_stepper = first_stepper // 2
# 	# print(f"second_stepper {second_stepper}")
# 	# total_stepper = first_stepper + second_stepper
# 	# print(f"total_steppr {total_stepper}")
# 	fd = 0
# 	sd = 0
# 	# for index,item in enumerate(items):
# 	# 	if index == (first_stepper-first_stepper) or index == first_stepper or index == (first_stepper + first_stepper):
# 	# 		fd = fd + items[index]
# 	# 	if  index == second_stepper or index == (second_stepper + second_stepper) or index == total_stepper:
# 	# 		sd = sd + items[index]
# 	return abs(fd-sd)

# a = diagonalDifference2([11,2,4,4,5,6,10,8,-12])