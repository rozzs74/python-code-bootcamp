def appendAndDelete(s, t, k):
    s_length = len(s)
    t_length = len(t)

    if s_length + t_length < k: return 'Yes'

    same = 0
    for s_l, t_l in zip(s, t):
        if s_l == t_l: same += 1
        else: break
   
    extra_s = s_length - same
    extra_t = t_length - same
    difference = extra_s + extra_t

    if difference <= k and difference % 2 == k % 2: return 'Yes'
    return 'No'


# a = appendAndDelete("hackerhappy", "hackerrank", 9)
a = appendAndDelete("aba", "aba", 7)	
print(a)
# a = appendAndDelete("ashley", "ash", 2)

