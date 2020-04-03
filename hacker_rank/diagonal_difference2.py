def diagonalDifference(items):
	items_length = len(items)
	print(items_length)
	# total_stepper = items_length - 1
	# modulo = items_length % 2
	# column = 0
	# if modulo == 1:
	# 	first_stepper = (total_stepper) // 2
	# 	column  = first_stepper - 1
	# 	second_stepper = column - 1
	# if modulo == 0:
	# 	first_stepper = (total_stepper) // 3 
	# 	column  = first_stepper - 1
	# 	second_stepper = column -  1

	# print(f"first_stepper {first_stepper}")
	# print(f"second_stepper {second_stepper}")
	# print(f"The matrix is {column} x {column}")
	# print(f"total_stepper {total_stepper}")
	fd = 0
	sd = 0
	# for index,item in enumerate(items):
	# 	# FD
	# 	if index == (first_stepper-first_stepper) or index == first_stepper or index == total_stepper:
	# 		print(items[index])
	# 		# fd = fd + items[index]
	# 	if  index == second_stepper or index == (second_stepper + second_stepper) or index == total_stepper:
	# 		# sd = sd + items[index]
	# 		print(items[index])
	return abs(fd-sd)


a = diagonalDifference([11, 2, 4, 4, 5, 6, 10, 8, -12])
# a = diagonalDifference([11,2,4,2,4,5,6,2,10,8,-12,2,1,1,1,2])
# print(a)
