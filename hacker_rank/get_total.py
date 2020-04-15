

def getTotalX(a, b):
	results=[]
	for i in range(1,max(b)+1):
		if all(i%anum==0 for anum in a) and all(bnum%i==0 for bnum in b):
			results.append(i)	
	return len(results)


result = getTotalX([2, 3], [2, 4])
print(result)