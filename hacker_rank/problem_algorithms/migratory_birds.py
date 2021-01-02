
def migratoryBirds(birds):
	birds_length = len(birds)
	lowest = min(birds)
	highest = max(birds)	
	count = {}
	i = 0
	for j in range(lowest, highest+1):
		count[str(j)] = 0
	while i < birds_length:
		sighted_birds = birds[:]
		print(f"sighted birds {sighted_birds}")
		i += 1
		#count[str(i)] = 0
		for bird in sighted_birds:
			print(f"Bird {bird}")	
			print(f"i {i}")	
			if bird == i:
				count[str(i)] += 1
		if i == birds_length:
			print(f"count {count}")
			print(f"sim c {max(count, key=count.get)}")
			return max(count, key=count.get)


#result = migratoryBirds([1, 4, 4, 4, 5, 3])
result = migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
# count = [0]*6
# for t in map(int,input().strip().split()):
#     count[t] += 1
# print(count.index(max(count)))
##def migratoryBirds(birds):
   # count = [0]*6
  #  for i in birds:
     #   count[i] += 1
    #return count.index(max(count))