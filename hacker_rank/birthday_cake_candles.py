
def birthdayCakeCandles(array):
	array_length = len(array)
	max_number = max(array)
	i = 0
	candle_to_blow = 0
	while array_length > 1:
		element = array[i]
		if element == max_number :
			candle_to_blow = candle_to_blow + 1
		i = i + 1
		if i == array_length:
			print(candle_to_blow)
			break
	return 1

a = birthdayCakeCandles([3,2,1,3])
