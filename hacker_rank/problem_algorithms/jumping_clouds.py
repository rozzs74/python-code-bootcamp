def jumpingOnClouds(clouds, jump_size):
	cloud_length= len(clouds)
	if jump_size <= 1 or jump_size <= cloud_length:
		e = 100
		i = 0
		cloud_length = len(clouds)
		while e != 0:
			i  = i + jump_size
			if i >= cloud_length :
				i = i % cloud_length
			e = e-1 - (clouds[i]*2)
			if i == 0 :
				break
		return e 

		# energy = 100
		# i = 0
		# while cloud_length > 1:
		# 	print(i)
		# 	# jr = clouds[(i + jump_size) % cloud_length]
		# 	# print(f"clouds {jr}")
		# 	# if jr == 0 :
		# 	# 	energy  = (energy - 1) - (energy - 2)
		# 	# if jr ==1 :
		# 	# 	energy  = (energy - 1) - (energy - 2)

		# 	i = i + 1
		# 	if i == cloud_length:
		# 		print(f"E {energy}")
		# 		return energy
	else:
		raise ValueError("nope")




# result = jumpingOnClouds([0,0,1,0],2)
result = jumpingOnClouds([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 1)  

    # e = 100
    # p = 0
    # while e != 0:
    #     p += k
    #     if p >= len(c) :
	# 		p = p%len(c)
    #     e = e-1 - (c[p]*2)
    #     if p == 0 : 
	# 		break 
