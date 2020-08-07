def appendAndDelete(s, t, k):
	a = k // 2
	print(a)
	b = 0
	for _ in range(0, k):
		if _ + a == k:
			b = _
			break
	s1 = s[:-b]
	t1 = t[-a:]
	fword = f"{s1}{t1}"

    
         




a = appendAndDelete("hackerhappy", "hackerrank", 9)
# a = appendAndDelete("ashley", "ash", 3)
# a = appendAndDelete("ashley", "ash", 2)