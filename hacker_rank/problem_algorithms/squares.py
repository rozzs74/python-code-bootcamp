import math
def squares(a, b):
	count = 0
	for _ in range(a, b+1):
		n = math.sqrt(_)
		if n.is_integer() == True:
			count += 1
	return count


a = squares(3, 9)
# a = squares(17, 24)
print(a)

# def squares(a, b):
#     count = 0
#     squares = 1
#     incre = 3
#     while squares <= b: 
#         if squares >= a: 
#             count += 1
#         squares = squares + incre
#         incre += 2
        
    
#     return count