def climbingLeaderBoard(scores, alice_scores):
    length_alice_score = len(alice_scores)
    i = 0
    alice_rank = []
    while length_alice_score > 1:
        alice_score = alice_scores[i]
        scores.append(alice_score)
        scores.sort(reverse=True)
        items = list(set(scores))
        items.sort(reverse=True)
        for score in scores:
            rank = items.index(score) + 1
            if score == alice_score:
                alice_rank.append(rank)
        scores.remove(alice_score)
        i += 1
        if i == length_alice_score:
            alice_rank = list(set(alice_rank))
            alice_rank.sort(reverse=True)
            break
# a = climbingLeaderBoard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
#6 4 2 1
a = climbingLeaderBoard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
# 6 5 4 2 1
print(a)

# push and rank then reset