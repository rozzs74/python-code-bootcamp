

#def divisibleSumPairs(arr_len, k, arr):
    #print(f"arr len {arr_len}")
    #print(f"k {k}")
    #print(f"arr {arr}")
    #i = 0
    #count = 0
    #while 0 < arr_len:
        #el = arr[i]
        #print(f"el {el}")
        #print(f"i {i}")
        #i += 1

        #el_arr = arr[:]
        #print(f"el_arr {el_arr}")

        #for j in el_arr:
            #ij = 0
            #if i < j:
              #  print(j)
             #   a = arr[i] + arr[j]
            #    print(f"a{a}")
            
        #if i == arr_len:
            #print(f"done count is {count}")
           # break



def divisibleSumPairs(n, k, ar):
    nums = [0] * k
    count = 0
    for ele in ar:
        modu = ele % k
        count += nums[(k - modu) % k]
        nums[modu] += 1
    return count

result = divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
print(result)
