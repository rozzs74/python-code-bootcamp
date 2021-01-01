#https://www.hackerrank.com/challenges/repeated-string/problem

# def repeated_string(s: str, n: int) -> int:
# 	if s == "a":
# 		return n
# 	string_length: int = len(s)
# 	print(f"String lenght {string_length}")
# 	print(f"Target length {n}")
# 	number_of_repeats: int = n // string_length + 1
# 	print(f"Number of repeats {number_of_repeats}")
# 	a_string_repeated: str = s * number_of_repeats
# 	print(f"String repeated {a_string_repeated}")
# 	new_string: str = a_string_repeated[:n]
# 	print(f"New String {new_string}")
# 	a_count: int = 0
# 	for letter in new_string:
# 		if letter == "a":
# 			a_count += 1
# 	return a_count



# count = repeated_string("abcac", 10)
# count = repeated_string("aba", 10)
# count = repeated_string("a", 1000000000000)
# print(count)

def repeatedString(s, n):
    c = s.count('a')
    div=n//len(s)
    if n%len(s)==0:
        c= c*div
    else:
        m = n%len(s)
        c= c*div+s[:m].count('a')
    return c