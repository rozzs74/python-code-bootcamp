#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def breakingRecords(scores):
	print(f"Maria current score {scores}")	
	no_games = len(scores)
	print(f"No of games played by Maria {no_games}")
	
	i = 0
	mins = []
	maxs  = []	
	while i < no_games:	
		score = scores[i]
		i += 1	
		print(f"Maria score {score} in game {i}")
		
		if i == 0:
			mins.append(score)
			maxs.append(score)
		
		if i == no_games:
			print(f"mins {mins}")
			print(f"max {maxs}")
			break	

	return 



result = breakingRecords([12, 24, 10, 24])
