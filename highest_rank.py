def highest_rank(arr):
    i = 0
    amount_arr = []
    for arr[i] in arr:
        if arr.count(arr[i]) > 1:
            if arr.count(arr[i]) == max(arr.count(arr[i])):
                amount_arr.append(arr[i])
        i += 1
print(highest_rank(([12, 10, 8, 12, 7, 6, 4, 10, 10])))
