


def cutTheSticks(arr):
    new_arr = sorted(arr)
    arr_length = len(new_arr)
    count = 0
    l = min(arr)
    h = max(arr)
    i = 0

    while i <= arr_length:
        col = []
        el = new_arr[i]
        if i == 0:
            print(f"a = {new_arr[i:arr_length]} el={el}")
            continue
        # des = new_arr[i:arr_length]
        # for j in des:
        #     diff = abs(el - j)
        #     if diff:
        #         col.append(diff)
        #     print(f"d={abs(el-j)} c={col}")

        i += 1
        if i == arr_length:
            break


a = cutTheSticks([5, 4, 4, 2, 2, 8])

# 5 4 4 2 2 8  

# 2 - 8 = 6 *
# 2 -2 = 0
# 2-2- = 0
# 2-4 = 2
# 2-4 = 2
# 2-5 = 3


# 6 2 2 3
# 2 - 6 = 4 *
# 2-2 = 0
# 2-2 =0
# 2-3 1

# 4 1
# 1 - 4  = 3   2 *
# 1 -1 = 0
#  3  0 

#  0 - 1 1