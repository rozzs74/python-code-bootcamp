# def climbingLeaderBoard(scores, alice_scores):
#     length_alice_score = len(alice_scores)
#     i = 0
    # alice_rank = []
#     while length_alice_score > 1:
#         items = []
#         alice_score = alice_scores[i]
#         scores.append(alice_score)
#         scores.sort(reverse=True)
#         print(scores)
#         # items = list(set(scores))
#         # items.sort(reverse=True)
#         for score in scores:
#             # print(score)
#             print(f"rank={scores.index(score) + 1} s={score}")
#             # rank = scores.index(score)  + 1
#             # if score == alice_score:
#             #     alice_rank.append(rank)
#         scores.remove(alice_score)
#         i += 1
#         if i == length_alice_score:
#             print(alice_rank)
#             # alice_rank = list(set(alice_rank))    
#             # alice_rank.sort(reverse=True)   
#             break
# # a = climbingLeaderBoard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
# #6 4 2 1

# print(a)

# push and rank then reset


# def climbingLeaderBoard(scores, alice_scores):  
#     alice_rank = []
#     i = 0
#     while len(alice_scores) >= 0:
#         alice_score = alice_scores[i]
#         scores.append(alice_score)
#         print(scores)
#         # scores.sort(reverse=True)
#         # sorted_unique = sorted(set(scores), reverse=True)
#         # for score in scores:
#         #     rank = sorted_unique.index(score)
#         #     if score == alice_score:
#         #         alice_rank.append(rank)
#         scores.remove(alice_score)
#         i += 1
#         if i == len(alice_scores):
#             # return sorted([x + 1 for x in alice_rank], reverse=True)
#             break
# print(a)
# 6 5 4 2 1

def climbingLeaderBoard(scores, alice_scores):
    leaderboard = sorted(set(scores), reverse = True)
    l = len(leaderboard)
    alice_rank = []
    i = 0
    for a in alice_scores:
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
        rank = l + 1
        alice_rank.append(rank)
        i += 1
        if i == len(alice_scores):
            return alice_rank
a = climbingLeaderBoard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
