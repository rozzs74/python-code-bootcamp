# MAKES TWENTY:
#  Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def make_twenty(x, y):
    return ((x + y) == 20) or ("20" in str(x) or "20" in str(y))  # my sol
    #return (n1+n2)==20 or n1==20 or n2==20 # protilla sol

result = make_twenty(10,10)
print(result)