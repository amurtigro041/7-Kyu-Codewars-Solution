def find_uniq(arr):
    list_UNIQUE = []
    i = 0
    for arr[i] in arr:
        if arr.count(arr[i]) == 1:
            list_UNIQUE.append(arr[i])
        i += 1
    return list_UNIQUE
    #result = [x for x in arr if arr.count(x) == 1]
    
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([3,3,5,5,1,2,3,2,2,1,11,4,5,7])) 
print(find_uniq([1,1,2,3,3,4,4,2,5,6,7]))