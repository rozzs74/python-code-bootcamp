#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def breakingRecords(scores):
	no_games = len(scores)
	i = 0
	h_score = min(scores)
	l_score  = max(scores)
	score_tally = {}
	all_game_highest_score = max(scores)
	all_game_lowest_score = min(scores)
	# print(all_game_lowest_score)

	h = []
	l = []
	while i < no_games:
		print(f"---START---")
		print(f"Game {i}")
		score_tally = scores[:i + 1]
		score = scores[i]
		print(f"Maria's score {score}")
		print(f"Maria's score tally {score_tally}")
		highest_score  = max(score_tally)
		print(f"Maria's highest score {highest_score}")
		lowest_score = min(score_tally)
		print(f"Maria's lowest score {lowest_score}")
		# print(f"Maria's score diff {highest_score - lowest_score}")
		print(f"---END---")


		# Expression for high score
		if score > lowest_score and score >= highest_score and scores[0] != all_game_highest_score:
			# print(score in h)
			if score in h:
				pass
			else:
				h.append(score)

		# if score < highest_score
		# 	l.append(score)			
		if score < highest_score and lowest_score >= score:
			print(f"ls {score}")
			l.append(score)
		i += 1

		if i == no_games:
			print(h, l)

			break
	return 

def breaking_records(score):
	min = max = score[0]
	min_count = max_count = 0
	for i in score[1:]:
		if i > max:
			max_count += 1
			max = i
		if i < min:
			min_count += 1
			min = i
	return max_count, min_count

# result = breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])
# result = breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
result = breaking_records([17,45,41,60,17,41,76,43,51,40,89,92,34,6,64,7,37,81,32,50])

print(result)
# result = breakingRecords([100,45,41,60,17,41,45,43,100,40,89,92,34,6,64,7,37,81,32,50])
# result = breakingRecords([12, 24, 10, 24])
