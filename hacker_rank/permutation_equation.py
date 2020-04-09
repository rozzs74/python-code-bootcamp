def permutationEquation(arr):
	n = len(arr)
	ans = []
	for i in range(0, n):    
		x = i + 1
		first_index = arr.index(x)
		second_index = arr.index(first_index + 1)
		ans.append(second_index + 1)
		if n == x:
			return ans


a = permutationEquation([2,3,1])
