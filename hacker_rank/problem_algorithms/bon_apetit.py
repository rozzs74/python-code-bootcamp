# Solution to works for int and smaller inputs
def compute(bill, k ,b):
    bills = len(bill)
    i = 0
    total = 0
    while bills > 1:
        el = bill[i]
        i += 1
        if el != bill[k]:
            total = total + el
        if i == bills:
            charge = total // 2
            if charge == b:
                print("Bon Appetit")
            else:
                diff = b - charge
                print(diff)
            break

a = compute([3, 10, 2, 9], 1, 12)

# Solution works all data types and larger inputs
def bonAppetit(bill, k, b):
    return b-(sum(bill)//2-bill[k]//2) or "Bon Appetit"
# https://www.thepoorcoder.com/hackerrank-bon-appetit-solution/